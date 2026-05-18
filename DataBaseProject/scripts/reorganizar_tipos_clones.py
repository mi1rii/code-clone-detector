#!/usr/bin/env python3
"""
Reorganiza/normaliza el dataset local basado en:
pares_clones/py/tipos_de_clones/{T1,T2,T3,T4}

Acciones:
1) valida existencia de T1..T4
2) opcional: renombra secuencialmente archivos por tipo
3) imprime conteos por carpeta
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TYPE_PREFIX = {
    "T1": "T1_",
    "T2": "T2_",
    "T3": "T3_",
    "T4": "T4_",
}


def contar_py(path: Path) -> int:
    return sum(1 for _ in path.glob("*.py"))


def renombrar_secuencial(tipo_dir: Path, tipo: str) -> int:
    prefijo = TYPE_PREFIX[tipo]
    archivos = sorted(tipo_dir.glob("*.py"))
    tmp_pairs: list[tuple[Path, Path]] = []

    # primer pase: mover a nombre temporal para evitar colisiones
    for idx, src in enumerate(archivos, start=1):
        tmp = tipo_dir / f"__tmp__{tipo}_{idx:06d}.py"
        src.rename(tmp)
        tmp_pairs.append((tmp, tipo_dir / f"{prefijo}{idx:06d}.py"))

    # segundo pase: nombre final
    for tmp, dst in tmp_pairs:
        tmp.rename(dst)

    return len(tmp_pairs)


def validar_nombres(tipo_dir: Path, tipo: str) -> tuple[int, int]:
    prefijo = TYPE_PREFIX[tipo]
    ok = 0
    bad = 0
    rgx = re.compile(rf"^{re.escape(prefijo)}\d{{6}}\.py$")
    for p in tipo_dir.glob("*.py"):
        if rgx.match(p.name):
            ok += 1
        else:
            bad += 1
    return ok, bad


def main() -> None:
    parser = argparse.ArgumentParser(description="Reorganiza T1/T2/T3/T4 en pares_clones/py/tipos_de_clones.")
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--renombrar-secuencial", action="store_true")
    args = parser.parse_args()

    base = args.dataset_dir.resolve()
    tipos_base = base / "pares_clones" / "py" / "tipos_de_clones"

    if not tipos_base.exists():
        raise FileNotFoundError(f"No existe {tipos_base}")

    tipos = ["T1", "T2", "T3", "T4"]
    for t in tipos:
        d = tipos_base / t
        if not d.exists():
            raise FileNotFoundError(f"No existe {d}")

    if args.renombrar_secuencial:
        for t in tipos:
            n = renombrar_secuencial(tipos_base / t, t)
            print(f"[ok] {t}: renombrados {n} archivos")

    for t in tipos:
        d = tipos_base / t
        total = contar_py(d)
        ok, bad = validar_nombres(d, t)
        print(f"[info] {t}: total={total}, nombre_ok={ok}, nombre_fuera_patron={bad}")

    print(f"[ok] validacion completada en: {tipos_base}")


if __name__ == "__main__":
    main()
