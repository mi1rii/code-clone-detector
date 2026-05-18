from __future__ import annotations

import keyword
import tokenize


def generalize_token(tok: tokenize.TokenInfo) -> str:
    """Map Python lexical tokens to Baker-style generalized symbols."""
    if tok.type == tokenize.NAME:
        if keyword.iskeyword(tok.string):
            return tok.string
        return "ID"
    if tok.type == tokenize.NUMBER:
        return "NUM"
    if tok.type == tokenize.STRING:
        return "STR"
    return tok.string


def generalize_tokens(tokens: list[tokenize.TokenInfo]) -> list[str]:
    return [generalize_token(tok) for tok in tokens]

