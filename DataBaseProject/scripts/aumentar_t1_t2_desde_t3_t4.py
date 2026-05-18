#!/usr/bin/env python3
from __future__ import annotations

import argparse
import io
import keyword
import random
import re
import tokenize
from pathlib import Path


PATRON_MARCADOR_LENGUAJE = re.compile(
    r"^\s*(python|java|javascript|c\+\+|cpp|ruby|go)\s*$",
    flags=re.IGNORECASE | re.MULTILINE,
)
PATRON_SEPARADOR_SNIPPETS = re.compile(r"\n\s*\n\s*\n+")
COMENTARIOS = [
    "nota de revision",
    "comentario sintetico",
    "equivalente funcional",
    "ajuste menor",
    "sin cambio de logica",
]


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


def insertar_comentarios(codigo: str, rng: random.Random) -> str:
    lineas = codigo.splitlines()
    if not lineas:
        return codigo
    n = rng.randint(1, 3)
    for _ in range(n):
        idx = rng.randint(0, len(lineas))
        lineas.insert(idx, f"# {rng.choice(COMENTARIOS)}")
    return "\n".join(lineas)


def renombrar_variables(codigo: str) -> str:
    builtins_basicos = {
        "len", "range", "min", "max", "sum", "list", "dict", "set", "tuple",
        "str", "int", "float", "bool", "print", "enumerate", "zip", "map",
        "filter", "any", "all", "abs", "sorted", "reversed", "isinstance",
    }
    mapeo: dict[str, str] = {}
    contador = 1

    out_tokens = []
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(codigo).readline))
    except (tokenize.TokenError, IndentationError):
        return codigo

    for tok in toks:
        if tok.type == tokenize.NAME:
            s = tok.string
            if (not keyword.iskeyword(s)) and (s not in builtins_basicos):
                if s not in mapeo:
                    mapeo[s] = f"var_{contador}"
                    contador += 1
                tok = tokenize.TokenInfo(tok.type, mapeo[s], tok.start, tok.end, tok.line)
        out_tokens.append(tok)
    try:
        return tokenize.untokenize(out_tokens)
    except Exception:
        return codigo


def max_id_en_carpeta(dir_path: Path, prefijo: str) -> int:
    max_id = 0
    rgx = re.compile(rf"^{re.escape(prefijo)}(\d+)\.py$")
    for p in dir_path.glob("*.py"):
        m = rgx.match(p.name)
        if m:
            max_id = max(max_id, int(m.group(1)))
    return max_id


def main() -> None:
    parser = argparse.ArgumentParser(description="Aumenta T1 y T2 desde snippets de T3/T4.")
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--target-count", type=int, default=2100)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    base = args.dataset_dir.resolve()
    tipos = base / "pares_clones" / "py" / "tipos_de_clones"
    t1 = tipos / "T1"
    t2 = tipos / "T2"
    t3 = tipos / "T3"
    t4 = tipos / "T4"
    rng = random.Random(args.seed)

    for d in [t1, t2, t3, t4]:
        if not d.exists():
            raise FileNotFoundError(f"No existe {d}")

    fuentes = []
    for d in [t3, t4]:
        for p in d.glob("*.py"):
            texto = p.read_text(encoding="utf-8", errors="replace")
            snippets = separar_snippets(texto)
            if snippets:
                fuentes.append(snippets[0].strip())
    if not fuentes:
        raise RuntimeError("No hay snippets fuente en T3/T4")
    rng.shuffle(fuentes)

    t1_actual = sum(1 for _ in t1.glob("*.py"))
    t2_actual = sum(1 for _ in t2.glob("*.py"))
    add_t1 = max(0, args.target_count - t1_actual)
    add_t2 = max(0, args.target_count - t2_actual)

    next_t1 = max_id_en_carpeta(t1, "1_Clone_") + 1
    next_t2 = max_id_en_carpeta(t2, "2_Clone_") + 1

    for i in range(add_t1):
        src = fuentes[i % len(fuentes)]
        a = src
        b = insertar_comentarios(src, rng)
        contenido = f"{a}\n\n\n{b}\n"
        (t1 / f"1_Clone_{next_t1}.py").write_text(contenido, encoding="utf-8")
        next_t1 += 1

    for i in range(add_t2):
        src = fuentes[i % len(fuentes)]
        a = src
        b = renombrar_variables(src)
        contenido = f"{a}\n\n\n{b}\n"
        (t2 / f"2_Clone_{next_t2}.py").write_text(contenido, encoding="utf-8")
        next_t2 += 1

    t1_final = sum(1 for _ in t1.glob("*.py"))
    t2_final = sum(1 for _ in t2.glob("*.py"))
    print(f"[ok] T1: {t1_actual} -> {t1_final} (agregados {add_t1})")
    print(f"[ok] T2: {t2_actual} -> {t2_final} (agregados {add_t2})")


if __name__ == "__main__":
    main()
