from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
import io
import re
import tokenize

import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_recall_fscore_support,
)
from sklearn.model_selection import GroupShuffleSplit
from sklearn.tree import DecisionTreeClassifier

from baker_similarity import baker_features_from_generalized_tokens
from baker_tokenizer import tokenize_and_generalize


COLUMNAS_METADATA = [
    "is_clone",
    "clone_type",
    "source_group",
    "filename",
    "file_path",
    "problem_id",
    "snippet_index_a",
    "snippet_index_b",
]

PATRON_MARCADOR_LENGUAJE = re.compile(
    r"^\s*(python|java|javascript|c\+\+|cpp|ruby|go)\s*$",
    flags=re.IGNORECASE | re.MULTILINE,
)
PATRON_SEPARADOR_SNIPPETS = re.compile(r"\n\s*\n\s*\n+")
PATRON_ESPACIOS = re.compile(r"[ \t]+")
PATRON_SALTOS = re.compile(r"\n{3,}")


@dataclass
class ResultadoSplit:
    train_idx: pd.Index
    val_idx: pd.Index
    test_idx: pd.Index


def resolve_dataset_root(cwd: Path | None = None) -> Path:
    base = Path.cwd() if cwd is None else cwd
    if (base / "clone_pairs_dataset_metadata.csv").exists():
        return base
    candidate = base / "DataBaseProject"
    if (candidate / "clone_pairs_dataset_metadata.csv").exists():
        return candidate
    raise FileNotFoundError("No se encontro clone_pairs_dataset_metadata.csv en cwd ni en cwd/DataBaseProject")


def cargar_metadata(ruta_csv: Path) -> pd.DataFrame:
    return pd.read_csv(ruta_csv)


def limpiar_metadata(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out = out[COLUMNAS_METADATA].copy()
    out["is_clone"] = pd.to_numeric(out["is_clone"], errors="coerce")
    out["problem_id"] = pd.to_numeric(out["problem_id"], errors="coerce")
    out["snippet_index_a"] = pd.to_numeric(out["snippet_index_a"], errors="coerce")
    out["snippet_index_b"] = pd.to_numeric(out["snippet_index_b"], errors="coerce")
    out = out.dropna(
        subset=["is_clone", "clone_type", "file_path", "problem_id", "snippet_index_a", "snippet_index_b"]
    ).copy()
    out["is_clone"] = out["is_clone"].astype(int)
    out["problem_id"] = out["problem_id"].astype(int)
    out["snippet_index_a"] = out["snippet_index_a"].astype(int)
    out["snippet_index_b"] = out["snippet_index_b"].astype(int)
    out = out[out["is_clone"] == 1].copy()
    return out


def separar_snippets(texto_archivo: str) -> list[str]:
    texto = texto_archivo.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not texto:
        return []
    bloques = [b.strip() for b in PATRON_MARCADOR_LENGUAJE.split(texto) if b.strip()]
    snippets: list[str] = []
    for bloque in bloques:
        partes = [p.strip() for p in PATRON_SEPARADOR_SNIPPETS.split(bloque) if p.strip()]
        if len(partes) > 1:
            snippets.extend(partes)
        else:
            snippets.append(bloque)
    if len(snippets) < 2:
        fallback = [p.strip() for p in PATRON_SEPARADOR_SNIPPETS.split(texto) if p.strip()]
        if len(fallback) > len(snippets):
            snippets = fallback
    return snippets


def normalizar_ruta_relativa(ruta: str) -> Path:
    return Path(str(ruta).replace("\\", "/"))


def reconstruir_pares(df_metadata: pd.DataFrame, ruta_dataset: Path) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    filas_ok = []
    filas_drop = []
    cache_snippets: dict[str, list[str] | None] = {}
    for fila in df_metadata.itertuples(index=False):
        ruta_rel = normalizar_ruta_relativa(str(fila.file_path))
        ruta_abs = ruta_dataset / ruta_rel
        clave = str(ruta_rel).lower()
        if clave not in cache_snippets:
            if not ruta_abs.exists():
                cache_snippets[clave] = None
            else:
                texto = ruta_abs.read_text(encoding="utf-8", errors="replace")
                cache_snippets[clave] = separar_snippets(texto)

        snippets = cache_snippets[clave]
        if snippets is None:
            filas_drop.append({**fila._asdict(), "drop_reason": "file_not_found"})
            continue

        idx_a = int(fila.snippet_index_a)
        idx_b = int(fila.snippet_index_b)
        if idx_a < 0 or idx_b < 0:
            filas_drop.append({**fila._asdict(), "drop_reason": "negative_snippet_index"})
            continue
        if idx_a >= len(snippets) or idx_b >= len(snippets):
            filas_drop.append({**fila._asdict(), "drop_reason": "snippet_index_out_of_range"})
            continue

        filas_ok.append(
            {
                **fila._asdict(),
                "resolved_path": str(ruta_abs),
                "snippet_count": len(snippets),
                "code_a": snippets[idx_a],
                "code_b": snippets[idx_b],
            }
        )

    df_ok = pd.DataFrame(filas_ok)
    df_drop = pd.DataFrame(filas_drop)
    resumen = {
        "metadata_rows": int(len(df_metadata)),
        "reconstructed_rows": int(len(df_ok)),
        "dropped_rows": int(len(df_drop)),
    }
    return df_ok, df_drop, resumen


def split_por_grupo(
    df: pd.DataFrame,
    group_col: str,
    target_col: str,
    seed: int = 42,
    train_size: float = 0.7,
    val_size: float = 0.15,
    test_size: float = 0.15,
) -> ResultadoSplit:
    proporcion_temp = val_size + test_size
    proporcion_test_rel = test_size / proporcion_temp
    gss_train = GroupShuffleSplit(n_splits=1, train_size=train_size, random_state=seed)
    idx_train_np, idx_temp_np = next(gss_train.split(df, y=df[target_col], groups=df[group_col]))

    df_temp = df.iloc[idx_temp_np]
    gss_temp = GroupShuffleSplit(n_splits=1, test_size=proporcion_test_rel, random_state=seed)
    idx_val_rel, idx_test_rel = next(gss_temp.split(df_temp, y=df_temp[target_col], groups=df_temp[group_col]))

    return ResultadoSplit(
        train_idx=df.index[idx_train_np],
        val_idx=df_temp.index[idx_val_rel],
        test_idx=df_temp.index[idx_test_rel],
    )


def asignar_split(df: pd.DataFrame, idx_train: pd.Index, idx_val: pd.Index, idx_test: pd.Index, nombre_columna: str = "split") -> pd.DataFrame:
    datos = df.copy()
    datos[nombre_columna] = "unassigned"
    datos.loc[idx_train, nombre_columna] = "train"
    datos.loc[idx_val, nombre_columna] = "val"
    datos.loc[idx_test, nombre_columna] = "test"
    return datos


def estadisticas_split(df: pd.DataFrame, split_col: str, target_col: str, group_col: str) -> list[dict[str, Any]]:
    resumen = []
    for nombre_split, df_split in df.groupby(split_col):
        conteos = df_split[target_col].value_counts().to_dict()
        resumen.append(
            {
                "split": nombre_split,
                "rows": int(len(df_split)),
                "unique_groups": int(df_split[group_col].nunique()),
                "class_distribution": {str(k): int(v) for k, v in conteos.items()},
            }
        )
    return resumen


def balancear_train(df_train: pd.DataFrame, target_col: str, estrategia: str = "none", seed: int = 42) -> tuple[pd.DataFrame, dict[str, Any]]:
    conteos = df_train[target_col].value_counts()
    info = {
        "strategy": estrategia,
        "target_col": target_col,
        "rows_before": int(len(df_train)),
        "class_distribution_before": {str(k): int(v) for k, v in conteos.items()},
    }

    if estrategia == "none" or len(conteos) <= 1:
        info["rows_after"] = int(len(df_train))
        info["class_distribution_after"] = info["class_distribution_before"]
        return df_train.copy(), info

    if estrategia == "undersample":
        n_obj = int(conteos.min())
        rep = False
    elif estrategia == "oversample":
        n_obj = int(conteos.max())
        rep = True
    else:
        info["rows_after"] = int(len(df_train))
        info["class_distribution_after"] = info["class_distribution_before"]
        return df_train.copy(), info

    partes = []
    for clase in conteos.index.tolist():
        df_clase = df_train[df_train[target_col] == clase]
        partes.append(df_clase.sample(n=n_obj, replace=rep, random_state=seed))

    out = pd.concat(partes, axis=0).sample(frac=1.0, random_state=seed).copy()
    c2 = out[target_col].value_counts()
    info["rows_after"] = int(len(out))
    info["class_distribution_after"] = {str(k): int(v) for k, v in c2.items()}
    return out, info


def quitar_comentarios(codigo: str) -> str:
    if not codigo.strip():
        return codigo
    try:
        salida = []
        lector = io.StringIO(codigo).readline
        for tok in tokenize.generate_tokens(lector):
            if tok.type == tokenize.COMMENT:
                continue
            salida.append(tok)
        return tokenize.untokenize(salida)
    except (tokenize.TokenError, IndentationError):
        return codigo


def normalizar_espacios(codigo: str) -> str:
    lineas = []
    for linea in codigo.splitlines():
        compacta = PATRON_ESPACIOS.sub(" ", linea).rstrip()
        lineas.append(compacta)
    normalizado = "\n".join(lineas).strip()
    normalizado = PATRON_SALTOS.sub("\n\n", normalizado)
    return normalizado


def preprocesar_codigo(codigo: str) -> str:
    return normalizar_espacios(quitar_comentarios(codigo))


def tokenizar_python(codigo: str) -> list[str]:
    if not codigo.strip():
        return []
    try:
        tokens = []
        lector = io.StringIO(codigo).readline
        excluir = {
            tokenize.ENCODING,
            tokenize.ENDMARKER,
            tokenize.NL,
            tokenize.NEWLINE,
            tokenize.INDENT,
            tokenize.DEDENT,
            tokenize.COMMENT,
        }
        for tok in tokenize.generate_tokens(lector):
            if tok.type in excluir:
                continue
            t = tok.string.strip()
            if t:
                tokens.append(t)
        return tokens
    except (tokenize.TokenError, IndentationError):
        return re.findall(r"[A-Za-z_]\w*|\d+|==|!=|<=|>=|[-+*/%=<>()[\]{}.,:;]", codigo)


def preparar_campos_par(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    code_a_clean = [preprocesar_codigo(x) for x in out["code_a"].astype(str)]
    code_b_clean = [preprocesar_codigo(x) for x in out["code_b"].astype(str)]
    tokens_a = [tokenizar_python(x) for x in code_a_clean]
    tokens_b = [tokenizar_python(x) for x in code_b_clean]
    baker_tokens_a = [tokenize_and_generalize(x) for x in code_a_clean]
    baker_tokens_b = [tokenize_and_generalize(x) for x in code_b_clean]

    out["code_a_clean"] = code_a_clean
    out["code_b_clean"] = code_b_clean
    out["tokens_a"] = tokens_a
    out["tokens_b"] = tokens_b
    out["token_text_a"] = [" ".join(t) for t in tokens_a]
    out["token_text_b"] = [" ".join(t) for t in tokens_b]
    out["baker_tokens_a"] = baker_tokens_a
    out["baker_tokens_b"] = baker_tokens_b
    out["clone_family_bin"] = out["clone_type"].map(
        {"type_I": "surface", "type_II": "surface", "type_III": "semantic", "type_IV": "semantic"}
    )
    return out


def similitud_jaccard(tokens_a: Iterable[str], tokens_b: Iterable[str]) -> float:
    set_a = set(tokens_a)
    set_b = set(tokens_b)
    if not set_a and not set_b:
        return 1.0
    union = set_a | set_b
    if not union:
        return 0.0
    return float(len(set_a & set_b) / len(union))


def similitud_dice(tokens_a: Iterable[str], tokens_b: Iterable[str]) -> float:
    set_a = set(tokens_a)
    set_b = set(tokens_b)
    if not set_a and not set_b:
        return 1.0
    denom = len(set_a) + len(set_b)
    if denom == 0:
        return 0.0
    return float(2.0 * len(set_a & set_b) / denom)


def ratio_overlap(tokens_a: Iterable[str], tokens_b: Iterable[str]) -> float:
    set_a = set(tokens_a)
    set_b = set(tokens_b)
    if not set_a and not set_b:
        return 1.0
    min_size = min(len(set_a), len(set_b))
    if min_size == 0:
        return 0.0
    return float(len(set_a & set_b) / min_size)


def ajustar_tfidf(df_train: pd.DataFrame) -> TfidfVectorizer:
    corpus = pd.concat([df_train["token_text_a"], df_train["token_text_b"]], axis=0)
    vector = TfidfVectorizer(
        tokenizer=str.split,
        preprocessor=None,
        token_pattern=None,
        lowercase=False,
        ngram_range=(1, 2),
        min_df=1,
    )
    vector.fit(corpus)
    return vector


def coseno_fila_a_fila(mat_a: sparse.spmatrix, mat_b: sparse.spmatrix) -> np.ndarray:
    producto = np.asarray(mat_a.multiply(mat_b).sum(axis=1)).ravel()
    norma_a = np.sqrt(np.asarray(mat_a.multiply(mat_a).sum(axis=1)).ravel())
    norma_b = np.sqrt(np.asarray(mat_b.multiply(mat_b).sum(axis=1)).ravel())
    denom = norma_a * norma_b
    denom[denom == 0.0] = 1e-12
    return producto / denom


def construir_features_baseline(df: pd.DataFrame, vector: TfidfVectorizer) -> pd.DataFrame:
    mat_a = vector.transform(df["token_text_a"])
    mat_b = vector.transform(df["token_text_b"])
    coseno = coseno_fila_a_fila(mat_a, mat_b)

    chars_a = df["code_a_clean"].str.len().astype(float)
    chars_b = df["code_b_clean"].str.len().astype(float)
    lineas_a = df["code_a_clean"].str.count("\n").astype(float) + 1.0
    lineas_b = df["code_b_clean"].str.count("\n").astype(float) + 1.0
    tokens_a = df["tokens_a"].apply(len).astype(float)
    tokens_b = df["tokens_b"].apply(len).astype(float)

    jaccard = [similitud_jaccard(a, b) for a, b in zip(df["tokens_a"], df["tokens_b"])]
    dice = [similitud_dice(a, b) for a, b in zip(df["tokens_a"], df["tokens_b"])]
    overlap = [ratio_overlap(a, b) for a, b in zip(df["tokens_a"], df["tokens_b"])]

    return pd.DataFrame(
        {
            "cosine_tfidf": coseno,
            "jaccard_tokens": jaccard,
            "dice_tokens": dice,
            "overlap_unique_tokens": overlap,
            "char_len_a": chars_a,
            "char_len_b": chars_b,
            "char_len_diff": (chars_a - chars_b).abs(),
            "line_count_a": lineas_a,
            "line_count_b": lineas_b,
            "line_count_diff": (lineas_a - lineas_b).abs(),
            "token_count_a": tokens_a,
            "token_count_b": tokens_b,
            "token_count_diff": (tokens_a - tokens_b).abs(),
        },
        index=df.index,
    )


def construir_features_baker(df: pd.DataFrame, min_match_len: int = 3) -> pd.DataFrame:
    rows = [
        baker_features_from_generalized_tokens(a, b, min_match_len=min_match_len)
        for a, b in zip(df["baker_tokens_a"], df["baker_tokens_b"])
    ]
    return pd.DataFrame(rows, index=df.index)


def construir_features_par(
    df: pd.DataFrame,
    vector: TfidfVectorizer,
    incluir_baker: bool = False,
    min_match_len: int = 3,
) -> pd.DataFrame:
    x_base = construir_features_baseline(df, vector)
    if not incluir_baker:
        return x_base
    x_baker = construir_features_baker(df, min_match_len=min_match_len)
    return pd.concat([x_base, x_baker], axis=1)


def evaluar_predicciones(y_true, y_pred, labels: list[str]) -> dict[str, Any]:
    acc = accuracy_score(y_true, y_pred)
    p_macro, r_macro, f1_macro, _ = precision_recall_fscore_support(
        y_true, y_pred, average="macro", zero_division=0
    )
    p_w, r_w, f1_w, _ = precision_recall_fscore_support(
        y_true, y_pred, average="weighted", zero_division=0
    )
    reporte_dict = classification_report(y_true, y_pred, labels=labels, output_dict=True, zero_division=0)
    reporte_texto = classification_report(y_true, y_pred, labels=labels, zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    return {
        "accuracy": float(acc),
        "precision_macro": float(p_macro),
        "recall_macro": float(r_macro),
        "f1_macro": float(f1_macro),
        "precision_weighted": float(p_w),
        "recall_weighted": float(r_w),
        "f1_weighted": float(f1_w),
        "confusion_matrix": cm.tolist(),
        "classification_report_dict": reporte_dict,
        "classification_report_text": reporte_texto,
    }


def entrenar_evaluar_decision_tree(
    datos_task: pd.DataFrame,
    columna_target: str,
    etiquetas: list[str],
    seed: int,
    estrategia_balanceo: str = "none",
    incluir_baker: bool = False,
    min_match_len: int = 3,
) -> dict[str, Any]:
    train_raw = datos_task[datos_task["split"] == "train"].copy()
    val = datos_task[datos_task["split"] == "val"].copy()
    test = datos_task[datos_task["split"] == "test"].copy()

    train_balanceado, info_balanceo = balancear_train(train_raw, columna_target, estrategia_balanceo, seed)

    vector_tfidf = ajustar_tfidf(train_balanceado)
    x_train = construir_features_par(train_balanceado, vector_tfidf, incluir_baker=incluir_baker, min_match_len=min_match_len)
    x_val = construir_features_par(val, vector_tfidf, incluir_baker=incluir_baker, min_match_len=min_match_len)
    x_test = construir_features_par(test, vector_tfidf, incluir_baker=incluir_baker, min_match_len=min_match_len)

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=12,
        min_samples_leaf=2,
        class_weight="balanced",
        random_state=seed,
    )
    model.fit(x_train, train_balanceado[columna_target])

    y_val = val[columna_target]
    y_test = test[columna_target]
    pred_val = model.predict(x_val)
    pred_test = model.predict(x_test)

    metricas_val = evaluar_predicciones(y_val, pred_val, labels=etiquetas)
    metricas_test = evaluar_predicciones(y_test, pred_test, labels=etiquetas)

    return {
        "info_balanceo": info_balanceo,
        "metricas_val": metricas_val,
        "metricas_test": metricas_test,
        "modelo": model,
        "num_features": int(x_train.shape[1]),
    }

