from __future__ import annotations

from typing import Sequence


def _to_initial_ranks(sequence: Sequence[str]) -> list[int]:
    uniq = {tok: i for i, tok in enumerate(sorted(set(sequence)))}
    return [uniq[tok] for tok in sequence]


def build_suffix_array(sequence: Sequence[str]) -> list[int]:
    """
    Build suffix array with a standard prefix-doubling algorithm.

    Time complexity is O(n log^2 n) due to Python sort in each doubling step.
    For snippet-scale token sequences this is typically fast enough.
    """
    n = len(sequence)
    if n == 0:
        return []
    if n == 1:
        return [0]

    sa = list(range(n))
    rank = _to_initial_ranks(sequence)
    tmp = [0] * n
    k = 1

    while True:
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))

        classes = 0
        tmp[sa[0]] = 0
        for i in range(1, n):
            prev = sa[i - 1]
            curr = sa[i]
            prev_key = (rank[prev], rank[prev + k] if prev + k < n else -1)
            curr_key = (rank[curr], rank[curr + k] if curr + k < n else -1)
            if curr_key != prev_key:
                classes += 1
            tmp[curr] = classes

        rank = tmp[:]
        if classes == n - 1:
            break
        k <<= 1

    return sa


def build_lcp_array(sequence: Sequence[str], suffix_array: Sequence[int]) -> list[int]:
    """
    Build LCP array with Kasai algorithm.

    LCP[i] is the common prefix length between suffix_array[i] and suffix_array[i-1].
    LCP[0] is always 0.
    """
    n = len(sequence)
    if n == 0:
        return []
    if n == 1:
        return [0]

    rank = [0] * n
    for i, suffix_start in enumerate(suffix_array):
        rank[suffix_start] = i

    lcp = [0] * n
    k = 0
    for i in range(n):
        ri = rank[i]
        if ri == 0:
            k = 0
            continue
        j = suffix_array[ri - 1]
        while i + k < n and j + k < n and sequence[i + k] == sequence[j + k]:
            k += 1
        lcp[ri] = k
        if k > 0:
            k -= 1

    return lcp

