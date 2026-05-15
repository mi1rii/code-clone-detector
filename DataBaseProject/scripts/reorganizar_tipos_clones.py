#!/usr/bin/env python3
"""
Reorganiza dataset de clones:
1) elimina true_semantic_clones/py/T1 actual
2) reconstruye T1 usando casos type_I detectados en false_semantic_clones/py
3) crea carpeta contenedora true_semantic_clones/py/tipos_de_clones con:
   - T1 (nuevo)
   - T2 (copiado desde false_semantic_clones/py/T2)
   - T3 (copiado desde true_semantic_clones/py/MT3)
   - T4 (copiado desde true_semantic_clones/py/T4)
"""

from __future__ import annotations

import argparse
import io
import re
import shutil
import tokenize
from pathlib import Path


PATRON_MARCADOR_LENGUAJE = re.compile(
    r"^\s*(python|java|javascript|c\+\+|cpp|ruby|go)\s*$",
    flags=re.IGNORECASE | re.MULTILINE,
)
PATRON_SEPARADOR_SNIPPETS = re.compile(r"\n\s*\n\s*\n+")


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


def tokens_significativos(codigo: str) -> list[tuple[int, str]]:
    excluir = {
        tokenize.ENCODING,
        tokenize.ENDMARKER,
        tokenize.NL,
        tokenize.NEWLINE,
        tokenize.INDENT,
        tokenize.DEDENT,
        tokenize.COMMENT,
    }
    out: list[tuple[int, str]] = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(codigo).readline):
            if tok.type in excluir:
                continue
            if not tok.string.strip():
                continue
            out.append((tok.type, tok.string))
    except (tokenize.TokenError, IndentationError):
        return []
    return out


def detectar_type1_en_false(false_py_dir: Path) -> list[tuple[int, Path]]:
    candidatos: list[tuple[int, Path]] = []
    for src in sorted(false_py_dir.glob("Gpt_false_pair_*.py")):
        texto = src.read_text(encoding="utf-8", errors="replace")
        snippets = separar_snippets(texto)
        if len(snippets) < 2:
            continue
        t0 = tokens_significativos(snippets[0])
        t1 = tokens_significativos(snippets[1])
        if t0 and t0 == t1:
            m = re.search(r"(\d+)\.py$", src.name)
            if not m:
                continue
            pid = int(m.group(1))
            candidatos.append((pid, src))
    candidatos.sort(key=lambda x: x[0])
    return candidatos


def limpiar_y_crear_directorio(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copiar_py(src_dir: Path, dst_dir: Path) -> int:
    dst_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for src in sorted(src_dir.glob("*.py")):
        shutil.copy2(src, dst_dir / src.name)
        count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Reorganiza T1/T2/T3/T4 en true_semantic.")
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    base_dir = args.dataset_dir.resolve()
    true_py = base_dir / "true_semantic_clones" / "py"
    false_py = base_dir / "false_semantic_clones" / "py"

    t1_true = true_py / "T1"
    t2_false = false_py / "T2"
    mt3_true = true_py / "MT3"
    t4_true = true_py / "T4"
    contenedor = true_py / "tipos_de_clones"

    if not false_py.exists():
        raise FileNotFoundError(f"No existe {false_py}")
    if not mt3_true.exists() or not t4_true.exists():
        raise FileNotFoundError("Faltan carpetas base MT3/T4 en true_semantic.")
    if not t2_false.exists():
        raise FileNotFoundError("No existe T2 en false_semantic. Corre primero el detector type_II.")

    # 1) reconstruir T1
    candidatos_t1 = detectar_type1_en_false(false_py)
    limpiar_y_crear_directorio(t1_true)
    for pid, src in candidatos_t1:
        dst = t1_true / f"1_Clone_{pid}.py"
        shutil.copy2(src, dst)

    # 2) crear contenedor organizado en true semantic
    limpiar_y_crear_directorio(contenedor)
    t1_out = contenedor / "T1"
    t2_out = contenedor / "T2"
    t3_out = contenedor / "T3"
    t4_out = contenedor / "T4"

    n1 = copiar_py(t1_true, t1_out)
    n2 = copiar_py(t2_false, t2_out)
    n3 = copiar_py(mt3_true, t3_out)
    n4 = copiar_py(t4_true, t4_out)

    print(f"[ok] T1 reconstruido desde false_semantic (type_I): {len(candidatos_t1)} archivos -> {t1_true}")
    print(f"[ok] contenedor creado: {contenedor}")
    print(f"[info] T1={n1}, T2={n2}, T3={n3}, T4={n4}")


if __name__ == "__main__":
    main()

