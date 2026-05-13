from __future__ import annotations

#reconstruimos code_a y code_b desde file_path y indices del metadata
import re
from pathlib import Path
from typing import Any

import pandas as pd


#definimos patrones para separar snippets de forma robusta
LANG_MARKER_RE = re.compile(
    r"(?im)^\s*(?:python|java|javascript|c\+\+|cpp|ruby|go)\s*$"
)
SNIPPET_SEP_RE = re.compile(
    r"\n(?:\s*\n){2,}(?=\s*(?:def|class|from|import|@)\b)"
)
FALLBACK_SEP_RE = re.compile(r"\n\s*\n\s*\n+")


def split_snippets(file_text: str) -> list[str]:
    #aplicamos la misma idea de segmentacion usada para generar pares originalmente
    text = file_text.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not text:
        return []

    #separamos bloques con marcadores de lenguaje cuando aparecen en el archivo
    blocks = [block.strip() for block in LANG_MARKER_RE.split(text) if block.strip()]
    snippets: list[str] = []

    #intentamos separar por bloques con saltos amplios antes de def class import
    for block in blocks:
        parts = [part.strip() for part in SNIPPET_SEP_RE.split(block) if part.strip()]
        snippets.extend(parts if len(parts) > 1 else [block])

    #usamos un respaldo por triples saltos de linea si no logramos al menos dos snippets
    if len(snippets) < 2:
        fallback_parts = [part.strip() for part in FALLBACK_SEP_RE.split(text) if part.strip()]
        if len(fallback_parts) > len(snippets):
            snippets = fallback_parts

    return snippets


def normalize_relative_path(raw_path: str) -> Path:
    #normalizamos separadores para que pathlib resuelva rutas de forma estable
    return Path(str(raw_path).replace("\\", "/"))


def reconstruct_pairs_from_metadata(
    metadata_df: pd.DataFrame,
    dataset_root: Path,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    #recorremos cada fila y validamos ruta lectura y rango de indices
    records: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []
    snippet_cache: dict[str, list[str]] = {}
    cache_path_failures: set[str] = set()

    for row in metadata_df.itertuples(index=False):
        #resolvemos la ruta del archivo que contiene los snippets de esta fila
        raw_path = str(row.file_path)
        rel_path = normalize_relative_path(raw_path)
        abs_path = dataset_root / rel_path

        #descartamos filas que apuntan a archivos inexistentes
        if not abs_path.exists():
            dropped.append(
                {
                    **row._asdict(),
                    "drop_reason": "missing_file_path",
                    "resolved_path": str(abs_path),
                }
            )
            continue

        #cacheamos snippets por archivo para evitar trabajo repetido
        cache_key = str(rel_path).lower()
        if cache_key not in snippet_cache and cache_key not in cache_path_failures:
            try:
                file_text = abs_path.read_text(encoding="utf-8", errors="replace")
                snippet_cache[cache_key] = split_snippets(file_text)
            except OSError:
                #registramos error de lectura y seguimos con la siguiente fila
                cache_path_failures.add(cache_key)
                dropped.append(
                    {
                        **row._asdict(),
                        "drop_reason": "file_read_error",
                        "resolved_path": str(abs_path),
                    }
                )
                continue

        #verificamos que el archivo tenga snippets ya cargados en cache
        snippets = snippet_cache.get(cache_key)
        if snippets is None:
            dropped.append(
                {
                    **row._asdict(),
                    "drop_reason": "snippet_cache_failure",
                    "resolved_path": str(abs_path),
                }
            )
            continue

        #validamos indices para no usar pares invalidos
        idx_a = int(row.snippet_index_a)
        idx_b = int(row.snippet_index_b)
        if idx_a == idx_b:
            dropped.append(
                {
                    **row._asdict(),
                    "drop_reason": "identical_snippet_indices",
                    "resolved_path": str(abs_path),
                    "snippet_count": len(snippets),
                }
            )
            continue
        if idx_a < 0 or idx_b < 0:
            dropped.append(
                {
                    **row._asdict(),
                    "drop_reason": "negative_snippet_index",
                    "resolved_path": str(abs_path),
                    "snippet_count": len(snippets),
                }
            )
            continue
        if idx_a >= len(snippets) or idx_b >= len(snippets):
            dropped.append(
                {
                    **row._asdict(),
                    "drop_reason": "snippet_index_out_of_range",
                    "resolved_path": str(abs_path),
                    "snippet_count": len(snippets),
                }
            )
            continue

        #guardamos la fila reconstruida con snippets y metadatos
        records.append(
            {
                **row._asdict(),
                "resolved_path": str(abs_path),
                "snippet_count": len(snippets),
                "code_a": snippets[idx_a],
                "code_b": snippets[idx_b],
            }
        )

    #dejamos dos dataframes para auditoria de calidad
    reconstructed_df = pd.DataFrame(records)
    dropped_df = pd.DataFrame(dropped)

    #resumimos conteos para reporte
    summary = {
        "metadata_rows": int(len(metadata_df)),
        "reconstructed_rows": int(len(reconstructed_df)),
        "dropped_rows": int(len(dropped_df)),
        "drop_reasons": (
            dropped_df["drop_reason"].value_counts().to_dict() if not dropped_df.empty else {}
        ),
    }
    return reconstructed_df, dropped_df, summary
