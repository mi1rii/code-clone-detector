from __future__ import annotations

#hacemos limpieza ligera y tokenizacion python sin romper la logica del codigo
import io
import re
import tokenize
from typing import Iterable


#declaramos reglas de normalizacion de espacios y lineas vacias
WHITESPACE_RE = re.compile(r"[ \t]+")
MULTI_NEWLINE_RE = re.compile(r"\n{3,}")


def strip_comments(code: str) -> str:
    #quitamos comentarios para reducir ruido lexical en las features
    if not code.strip():
        return code

    try:
        output_tokens: list[tokenize.TokenInfo] = []
        reader = io.StringIO(code).readline
        for tok in tokenize.generate_tokens(reader):
            if tok.type == tokenize.COMMENT:
                continue
            output_tokens.append(tok)
        return tokenize.untokenize(output_tokens)
    except (tokenize.TokenError, IndentationError):
        #dejamos el codigo original si tokenizar falla en snippets ruidosos
        return code


def normalize_whitespace(code: str) -> str:
    #compactamos espacios repetidos y limitamos saltos de linea consecutivos
    lines = []
    for line in code.splitlines():
        compact = WHITESPACE_RE.sub(" ", line).rstrip()
        lines.append(compact)
    normalized = "\n".join(lines).strip()
    normalized = MULTI_NEWLINE_RE.sub("\n\n", normalized)
    return normalized


def preprocess_code(code: str) -> str:
    #aplicamos el preprocesamiento minimo que acordamos para el baseline
    no_comments = strip_comments(code)
    return normalize_whitespace(no_comments)


def tokenize_python_code(code: str) -> list[str]:
    #tokenizamos con la libreria tokenize para respetar mejor sintaxis python
    if not code.strip():
        return []

    try:
        tokens: list[str] = []
        reader = io.StringIO(code).readline
        skip_types = {
            tokenize.ENCODING,
            tokenize.ENDMARKER,
            tokenize.NL,
            tokenize.NEWLINE,
            tokenize.INDENT,
            tokenize.DEDENT,
            tokenize.COMMENT,
        }
        for tok in tokenize.generate_tokens(reader):
            if tok.type in skip_types:
                continue
            text = tok.string.strip()
            if text:
                tokens.append(text)
        return tokens
    except (tokenize.TokenError, IndentationError):
        #usamos un respaldo regex cuando el snippet tiene formato incompleto
        return re.findall(r"[A-Za-z_]\w*|\d+|==|!=|<=|>=|[-+*/%=<>()[\]{},.:;]", code)


def jaccard_similarity(tokens_a: Iterable[str], tokens_b: Iterable[str]) -> float:
    #medimos interseccion sobre union de tokens unicos
    set_a = set(tokens_a)
    set_b = set(tokens_b)
    if not set_a and not set_b:
        return 1.0
    union = set_a | set_b
    if not union:
        return 0.0
    return float(len(set_a & set_b) / len(union))


def overlap_ratio(tokens_a: Iterable[str], tokens_b: Iterable[str]) -> float:
    #medimos que tanto se cubre el conjunto mas pequeno de tokens
    set_a = set(tokens_a)
    set_b = set(tokens_b)
    if not set_a and not set_b:
        return 1.0
    min_size = min(len(set_a), len(set_b))
    if min_size == 0:
        return 0.0
    return float(len(set_a & set_b) / min_size)
