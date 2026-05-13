from __future__ import annotations

#construimos representaciones de texto y features numericas del par de snippets
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer

from .preprocessing import jaccard_similarity, overlap_ratio, preprocess_code, tokenize_python_code


def prepare_pair_text_fields(df: pd.DataFrame) -> pd.DataFrame:
    #limpiamos cada snippet y generamos tokens para ambos lados del par
    result = df.copy()

    code_a_clean = [preprocess_code(text) for text in result["code_a"].astype(str)]
    code_b_clean = [preprocess_code(text) for text in result["code_b"].astype(str)]

    tokens_a = [tokenize_python_code(text) for text in code_a_clean]
    tokens_b = [tokenize_python_code(text) for text in code_b_clean]

    #guardamos campos intermedios para trazabilidad y para calcular features
    result["code_a_clean"] = code_a_clean
    result["code_b_clean"] = code_b_clean
    result["tokens_a"] = tokens_a
    result["tokens_b"] = tokens_b
    result["token_text_a"] = [" ".join(tokens) for tokens in tokens_a]
    result["token_text_b"] = [" ".join(tokens) for tokens in tokens_b]
    return result


def fit_tfidf_vectorizer(train_df: pd.DataFrame) -> TfidfVectorizer:
    #ajustamos tf idf solo con train para evitar leakage hacia val y test
    corpus = pd.concat([train_df["token_text_a"], train_df["token_text_b"]], axis=0)
    vectorizer = TfidfVectorizer(
        tokenizer=str.split,
        preprocessor=None,
        token_pattern=None,
        lowercase=False,
        ngram_range=(1, 2),
        min_df=1,
    )
    vectorizer.fit(corpus)
    return vectorizer


def rowwise_cosine_similarity(matrix_a: sparse.spmatrix, matrix_b: sparse.spmatrix) -> np.ndarray:
    #calculamos coseno fila por fila entre snippet a y snippet b del mismo par
    dot = np.asarray(matrix_a.multiply(matrix_b).sum(axis=1)).ravel()
    norm_a = np.sqrt(np.asarray(matrix_a.multiply(matrix_a).sum(axis=1)).ravel())
    norm_b = np.sqrt(np.asarray(matrix_b.multiply(matrix_b).sum(axis=1)).ravel())
    denom = norm_a * norm_b
    denom[denom == 0.0] = 1e-12
    return dot / denom


def build_pair_features(df: pd.DataFrame, vectorizer: TfidfVectorizer) -> pd.DataFrame:
    #transformamos snippets a espacio tf idf y derivamos features de similitud y tamano
    matrix_a = vectorizer.transform(df["token_text_a"])
    matrix_b = vectorizer.transform(df["token_text_b"])
    cosine_values = rowwise_cosine_similarity(matrix_a, matrix_b)

    char_len_a = df["code_a_clean"].str.len().astype(float)
    char_len_b = df["code_b_clean"].str.len().astype(float)
    line_count_a = df["code_a_clean"].str.count("\n").astype(float) + 1.0
    line_count_b = df["code_b_clean"].str.count("\n").astype(float) + 1.0
    token_count_a = df["tokens_a"].apply(len).astype(float)
    token_count_b = df["tokens_b"].apply(len).astype(float)

    jaccard_values = [
        jaccard_similarity(tokens_a, tokens_b)
        for tokens_a, tokens_b in zip(df["tokens_a"], df["tokens_b"])
    ]
    overlap_values = [
        overlap_ratio(tokens_a, tokens_b)
        for tokens_a, tokens_b in zip(df["tokens_a"], df["tokens_b"])
    ]

    #consolidamos todas las features numericas en una sola tabla
    features_df = pd.DataFrame(
        {
            "cosine_tfidf": cosine_values,
            "jaccard_tokens": jaccard_values,
            "overlap_unique_tokens": overlap_values,
            "char_len_a": char_len_a,
            "char_len_b": char_len_b,
            "char_len_diff": (char_len_a - char_len_b).abs(),
            "line_count_a": line_count_a,
            "line_count_b": line_count_b,
            "line_count_diff": (line_count_a - line_count_b).abs(),
            "token_count_a": token_count_a,
            "token_count_b": token_count_b,
            "token_count_diff": (token_count_a - token_count_b).abs(),
        },
        index=df.index,
    )
    return features_df


def save_feature_splits(
    split_to_features: dict[str, pd.DataFrame],
    split_to_targets: dict[str, pd.Series],
    output_dir: Path,
    target_name: str,
) -> None:
    #exportamos features por split para inspeccion y trazabilidad experimental
    output_dir.mkdir(parents=True, exist_ok=True)
    for split_name, features_df in split_to_features.items():
        export_df = features_df.copy()
        export_df[target_name] = split_to_targets[split_name].values
        export_df.to_csv(output_dir / f"{split_name}_features.csv", index=False, encoding="utf-8")
