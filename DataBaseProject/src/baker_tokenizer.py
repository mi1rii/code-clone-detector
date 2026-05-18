from __future__ import annotations

import io
import re
import tokenize

from baker_generalizer import generalize_tokens


EXCLUDED_TOKEN_TYPES = {
    tokenize.ENCODING,
    tokenize.ENDMARKER,
    tokenize.NL,
    tokenize.NEWLINE,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.COMMENT,
}


def tokenize_python_code(code: str) -> list[tokenize.TokenInfo]:
    """Tokenize Python code with stdlib tokenize, returning significant tokens."""
    if not code.strip():
        return []

    out: list[tokenize.TokenInfo] = []
    reader = io.StringIO(code).readline
    try:
        for tok in tokenize.generate_tokens(reader):
            if tok.type in EXCLUDED_TOKEN_TYPES:
                continue
            if not tok.string.strip():
                continue
            out.append(tok)
    except (tokenize.TokenError, IndentationError):
        # Fallback keeps pipeline robust for malformed snippets.
        parts = re.findall(r"[A-Za-z_]\w*|\d+|==|!=|<=|>=|[-+*/%=<>()[\]{}.,:;]", code)
        out = [tokenize.TokenInfo(tokenize.NAME, p, (0, 0), (0, 0), "") for p in parts]
    return out


def tokenize_and_generalize(code: str) -> list[str]:
    return generalize_tokens(tokenize_python_code(code))

