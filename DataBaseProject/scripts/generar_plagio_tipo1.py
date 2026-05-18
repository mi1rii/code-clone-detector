#!/usr/bin/env python3
"""
Genera ejemplos sinteticos de plagio type_I a partir de un solo snippet:
- toma un codigo fuente
- inserta comentarios aleatorios
- duplica el snippet (par 0,1) dentro del mismo archivo
- actualiza clone_pairs_dataset_metadata.csv

Tambien puede limpiar todos los sinteticos generados previamente.
"""

from __future__ import annotations

import argparse
import csv
import random
import re
from pathlib import Path
from typing import Iterable


PATRON_MARCADOR_LENGUAJE = re.compile(
    r"^\s*(python|java|javascript|c\+\+|cpp|ruby|go)\s*$",
    flags=re.IGNORECASE | re.MULTILINE,
)
PATRON_SEPARADOR_SNIPPETS = re.compile(r"\n\s*\n\s*\n+")

METADATA_COLS = [
    "is_clone",
    "clone_type",
    "source_group",
    "filename",
    "file_path",
    "problem_id",
    "snippet_index_a",
    "snippet_index_b",
]

SOURCE_GROUP_SYNTH = "pares_t1_synth"
CLONE_TYPE_SYNTH = "type_I"
SYNTH_REL_DIR = Path("pares_clones") / "py" / "tipos_de_clones" / "T1_SYNTH"

COMENTARIOS = [
    "revision de estilo",
    "nota sintetica",
    "comentario auto generado",
    "ajuste menor",
    "mantener logica",
    "sin cambios funcionales",
    "version balanceo",
    "bloque equivalente",
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


def cargar_metadata(path_csv: Path) -> list[dict[str, str]]:
    with path_csv.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def guardar_metadata(path_csv: Path, rows: Iterable[dict[str, str]]) -> None:
    with path_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=METADATA_COLS)
        writer.writeheader()
        writer.writerows(rows)


def limpiar_sinteticos(base_dir: Path, metadata_rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], int, int]:
    # compat: limpia tanto el directorio actual como uno legado.
    dirs_limpiar = [
        base_dir / SYNTH_REL_DIR,
        base_dir / "true_semantic_clones" / "py" / "T1_SYNTH",  # legado
    ]
    borrados_archivos = 0
    for synth_dir in dirs_limpiar:
        if synth_dir.exists():
            for py in synth_dir.glob("*.py"):
                py.unlink()
                borrados_archivos += 1
            if not any(synth_dir.iterdir()):
                synth_dir.rmdir()

    filtrado = [
        r
        for r in metadata_rows
        if r.get("source_group") not in {SOURCE_GROUP_SYNTH, "true_semantic_t1_synthetic", "true_semantic_t1"}
    ]
    borradas_filas = len(metadata_rows) - len(filtrado)
    return filtrado, borrados_archivos, borradas_filas


def escoger_snippets_fuente(base_dir: Path, rng: random.Random) -> list[str]:
    roots = [
        base_dir / "pares_clones" / "py" / "tipos_de_clones",
        base_dir / "false_semantic_clones" / "py",  # legado
        base_dir / "true_semantic_clones" / "py",   # legado
    ]
    snippets: list[str] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.py"):
            # evita auto-reusar sinteticos viejos
            if "T1_SYNTH" in path.parts:
                continue
            texto = path.read_text(encoding="utf-8", errors="replace")
            for s in separar_snippets(texto):
                if len(s.strip()) >= 40:
                    snippets.append(s.strip())

    rng.shuffle(snippets)
    return snippets


def insertar_comentarios_random(codigo: str, rng: random.Random) -> str:
    lineas = codigo.splitlines()
    if not lineas:
        return codigo

    n_comentarios = rng.randint(1, 3)
    for _ in range(n_comentarios):
        idx = rng.randint(0, len(lineas))
        texto = rng.choice(COMENTARIOS)
        lineas.insert(idx, f"# {texto}")
    return "\n".join(lineas).strip()


def siguiente_problem_id(metadata_rows: list[dict[str, str]]) -> int:
    max_id = 0
    for r in metadata_rows:
        try:
            max_id = max(max_id, int(r["problem_id"]))
        except (ValueError, KeyError):
            continue
    return max_id + 1


def contar_clases(metadata_rows: list[dict[str, str]]) -> dict[str, int]:
    out = {"0": 0, "1": 0}
    for r in metadata_rows:
        if r.get("is_clone") in out:
            out[r["is_clone"]] += 1
    return out


def contar_tipos_positivos(metadata_rows: list[dict[str, str]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for r in metadata_rows:
        if r.get("is_clone") != "1":
            continue
        t = r.get("clone_type", "")
        out[t] = out.get(t, 0) + 1
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Generar plagio sintetico type_I y actualizar metadata.")
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--num-new", type=int, default=0, help="Cantidad de nuevos archivos type_I a crear.")
    parser.add_argument(
        "--usar-diferencia-absoluta-task-a",
        action="store_true",
        help="Usa |is_clone_1 - is_clone_0| como cantidad a generar.",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--limpiar-sinteticos", action="store_true", help="Borra sinteticos previos (carpeta y CSV).")
    parser.add_argument(
        "--objetivo-t1-promedio-t3-t4",
        action="store_true",
        help="Define num_new para que el total type_I quede en el promedio entre type_III y type_IV.",
    )
    args = parser.parse_args()

    base_dir: Path = args.dataset_dir.resolve()
    metadata_path = base_dir / "clone_pairs_dataset_metadata.csv"
    if not metadata_path.exists():
        raise FileNotFoundError(f"No existe metadata: {metadata_path}")

    rng = random.Random(args.seed)
    rows = cargar_metadata(metadata_path)

    if args.limpiar_sinteticos:
        rows, borrados_archivos, borradas_filas = limpiar_sinteticos(base_dir, rows)
        guardar_metadata(metadata_path, rows)
        print(f"[ok] limpieza sinteticos -> archivos borrados: {borrados_archivos}, filas borradas: {borradas_filas}")
        if (
            args.num_new <= 0
            and not args.usar_diferencia_absoluta_task_a
            and not args.objetivo_t1_promedio_t3_t4
        ):
            conteos = contar_clases(rows)
            print(f"[info] conteos actuales: is_clone=1 -> {conteos['1']}, is_clone=0 -> {conteos['0']}")
            return

    if args.objetivo_t1_promedio_t3_t4:
        tipos = contar_tipos_positivos(rows)
        t3 = tipos.get("type_III", 0)
        t4 = tipos.get("type_IV", 0)
        t1_actual = tipos.get("type_I", 0)
        objetivo = int(round((t3 + t4) / 2))
        num_new = max(0, objetivo - t1_actual)
        print(f"[info] type_III={t3}, type_IV={t4}, type_I_actual={t1_actual}, type_I_objetivo={objetivo}")
    elif args.usar_diferencia_absoluta_task_a:
        conteos = contar_clases(rows)
        num_new = abs(conteos["1"] - conteos["0"])
    else:
        num_new = args.num_new

    if num_new <= 0:
        conteos = contar_clases(rows)
        print("[ok] sin cambios (num_new <= 0)")
        print(f"[info] conteos actuales: is_clone=1 -> {conteos['1']}, is_clone=0 -> {conteos['0']}")
        return

    synth_dir = base_dir / SYNTH_REL_DIR
    synth_dir.mkdir(parents=True, exist_ok=True)

    candidatos = escoger_snippets_fuente(base_dir, rng)
    if not candidatos:
        raise RuntimeError("No hay snippets fuente para generar sinteticos.")

    pid = siguiente_problem_id(rows)
    nuevos: list[dict[str, str]] = []

    for i in range(num_new):
        fuente = candidatos[i % len(candidatos)]
        snippet_a = fuente.strip()
        snippet_b = insertar_comentarios_random(snippet_a, rng)

        nombre = f"1_Clone_{pid}.py"
        rel_path = SYNTH_REL_DIR / nombre
        abs_path = base_dir / rel_path

        contenido = f"{snippet_a}\n\n\n{snippet_b}\n"
        abs_path.write_text(contenido, encoding="utf-8")

        nuevos.append(
            {
                "is_clone": "1",
                "clone_type": CLONE_TYPE_SYNTH,
                "source_group": SOURCE_GROUP_SYNTH,
                "filename": nombre,
                "file_path": str(rel_path).replace("/", "\\"),
                "problem_id": str(pid),
                "snippet_index_a": "0",
                "snippet_index_b": "1",
            }
        )
        pid += 1

    rows.extend(nuevos)
    guardar_metadata(metadata_path, rows)

    conteos_finales = contar_clases(rows)
    print(f"[ok] sinteticos creados: {len(nuevos)} en {synth_dir}")
    print(f"[info] conteos finales: is_clone=1 -> {conteos_finales['1']}, is_clone=0 -> {conteos_finales['0']}")
    print("[nota] este script agrega positivos (plagio type_I); no agrega negativos.")


if __name__ == "__main__":
    main()
