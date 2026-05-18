#!/usr/bin/env python3
"""
Detecta candidatos type_II usando filas de metadata:
- compara snippet 0 vs 1 por archivo
- considera type_II cuando la estructura tokenizada normalizada coincide
  y existen cambios de identificadores o literales
- puede copiar candidatos a una carpeta destino (por defecto dentro de pares_clones)
"""

from __future__ import annotations

import argparse
import csv
import io
import keyword
import re
import tokenize
from dataclasses import dataclass
from pathlib import Path


PATRON_MARCADOR_LENGUAJE = re.compile(
    r"^\s*(python|java|javascript|c\+\+|cpp|ruby|go)\s*$",
    flags=re.IGNORECASE | re.MULTILINE,
)
PATRON_SEPARADOR_SNIPPETS = re.compile(r"\n\s*\n\s*\n+")


@dataclass
class AnalisisPar:
    es_tipo2: bool
    razon: str
    id_diff_count: int
    literal_diff_count: int
    token_count: int


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
        partes_fallback = [p.strip() for p in PATRON_SEPARADOR_SNIPPETS.split(texto) if p.strip()]
        if len(partes_fallback) > len(snippets):
            snippets = partes_fallback
    return snippets


def tokens_significativos(codigo: str) -> list[tokenize.TokenInfo]:
    excluir = {
        tokenize.ENCODING,
        tokenize.ENDMARKER,
        tokenize.NL,
        tokenize.NEWLINE,
        tokenize.INDENT,
        tokenize.DEDENT,
        tokenize.COMMENT,
    }
    out: list[tokenize.TokenInfo] = []
    lector = io.StringIO(codigo).readline
    try:
        for tok in tokenize.generate_tokens(lector):
            if tok.type in excluir:
                continue
            if not tok.string.strip():
                continue
            out.append(tok)
    except (tokenize.TokenError, IndentationError):
        return []
    return out


def es_identificador(tok: tokenize.TokenInfo) -> bool:
    return tok.type == tokenize.NAME and not keyword.iskeyword(tok.string)


def token_norm(tok: tokenize.TokenInfo) -> str:
    if es_identificador(tok):
        return "ID"
    if tok.type == tokenize.NUMBER:
        return "NUM"
    if tok.type == tokenize.STRING:
        return "STR"
    return tok.string


def analizar_par_tipo2(snippet_a: str, snippet_b: str) -> AnalisisPar:
    toks_a = tokens_significativos(snippet_a)
    toks_b = tokens_significativos(snippet_b)

    if not toks_a or not toks_b:
        return AnalisisPar(False, "tokenizacion_vacia", 0, 0, 0)
    if len(toks_a) != len(toks_b):
        return AnalisisPar(False, "longitud_tokens_distinta", 0, 0, min(len(toks_a), len(toks_b)))

    norm_a = [token_norm(t) for t in toks_a]
    norm_b = [token_norm(t) for t in toks_b]
    if norm_a != norm_b:
        return AnalisisPar(False, "estructura_normalizada_distinta", 0, 0, len(norm_a))

    id_diff = 0
    lit_diff = 0
    for ta, tb in zip(toks_a, toks_b):
        if es_identificador(ta) and es_identificador(tb) and ta.string != tb.string:
            id_diff += 1
        elif ta.type in {tokenize.NUMBER, tokenize.STRING} and tb.type == ta.type and ta.string != tb.string:
            lit_diff += 1

    if id_diff == 0 and lit_diff == 0:
        return AnalisisPar(False, "sin_cambio_id_ni_literal", 0, 0, len(norm_a))
    return AnalisisPar(True, "ok_tipo2", id_diff, lit_diff, len(norm_a))


def main() -> None:
    parser = argparse.ArgumentParser(description="Detecta posibles type_II desde metadata.")
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--source-group", default="pares_t2")
    parser.add_argument("--copiar-a-t2", action="store_true")
    parser.add_argument("--limpiar-t2", action="store_true")
    parser.add_argument(
        "--destino-rel",
        default=r"pares_clones\py\tipos_de_clones\T2_detectados",
        help="Ruta relativa bajo dataset-dir para copiar candidatos.",
    )
    args = parser.parse_args()

    base_dir = args.dataset_dir.resolve()
    t2_dir = base_dir / Path(args.destino_rel.replace("\\", "/"))
    metadata_path = base_dir / "clone_pairs_dataset_metadata.csv"
    reporte_path = base_dir / "scripts" / "reporte_false_semantic_tipo2.csv"

    if args.limpiar_t2 and t2_dir.exists():
        for p in t2_dir.glob("*.py"):
            p.unlink()
        if not any(t2_dir.iterdir()):
            t2_dir.rmdir()

    if not metadata_path.exists():
        raise FileNotFoundError(f"No existe: {metadata_path}")

    false_rows: list[dict[str, str]] = []
    with metadata_path.open("r", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("source_group") == args.source_group:
                false_rows.append(r)

    candidatos: list[tuple[dict[str, str], AnalisisPar]] = []
    no_candidatos = 0
    errores = 0

    for row in false_rows:
        rel = Path(row["file_path"].replace("\\", "/"))
        abs_path = base_dir / rel
        if not abs_path.exists():
            errores += 1
            continue
        texto = abs_path.read_text(encoding="utf-8", errors="replace")
        snippets = separar_snippets(texto)
        if len(snippets) < 2:
            errores += 1
            continue
        ana = analizar_par_tipo2(snippets[0], snippets[1])
        if ana.es_tipo2:
            candidatos.append((row, ana))
        else:
            no_candidatos += 1

    candidatos.sort(key=lambda x: int(x[0]["problem_id"]))

    # reporte
    reporte_path.parent.mkdir(parents=True, exist_ok=True)
    with reporte_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "problem_id",
                "filename_original",
                "file_path_original",
                "id_diff_count",
                "literal_diff_count",
                "token_count",
                "razon",
            ],
        )
        w.writeheader()
        for row, ana in candidatos:
            w.writerow(
                {
                    "problem_id": row["problem_id"],
                    "filename_original": row["filename"],
                    "file_path_original": row["file_path"],
                    "id_diff_count": ana.id_diff_count,
                    "literal_diff_count": ana.literal_diff_count,
                    "token_count": ana.token_count,
                    "razon": ana.razon,
                }
            )

    copiados = 0
    if args.copiar_a_t2:
        t2_dir.mkdir(parents=True, exist_ok=True)
        for row, _ in candidatos:
            src = base_dir / Path(row["file_path"].replace("\\", "/"))
            pid = int(row["problem_id"])
            dst = t2_dir / f"2_Clone_{pid}.py"
            dst.write_text(src.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")
            copiados += 1

    print(f"[info] source_group revisado ({args.source_group}): {len(false_rows)}")
    print(f"[info] candidatos type_II: {len(candidatos)}")
    print(f"[info] no candidatos: {no_candidatos}")
    print(f"[info] errores lectura/tokenizacion: {errores}")
    if args.copiar_a_t2:
        print(f"[ok] copiados a T2: {copiados} -> {t2_dir}")
    print(f"[ok] reporte: {reporte_path}")


if __name__ == "__main__":
    main()
