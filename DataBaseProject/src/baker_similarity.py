from __future__ import annotations

from dataclasses import dataclass

from baker_suffix_array import build_lcp_array, build_suffix_array


@dataclass(frozen=True)
class BakerMatch:
    start_a: int
    start_b: int
    length: int


def _origin_of_index(idx: int, len_a: int, len_b: int) -> int:
    # 0 => seq A, 1 => seq B, -1 => separator region
    sep_a = len_a
    sep_b = len_a + 1 + len_b
    if idx < sep_a:
        return 0
    if idx == sep_a or idx == sep_b:
        return -1
    if sep_a < idx < sep_b:
        return 1
    return -1


def _to_local_index(global_idx: int, len_a: int) -> int:
    # Sequence B starts after [A + sep]
    return global_idx - (len_a + 1)


def _extract_candidate_matches(tokens_a: list[str], tokens_b: list[str], min_match_len: int) -> list[BakerMatch]:
    if not tokens_a or not tokens_b:
        return []

    sep_a = "__A_END_UNIQUE__"
    sep_b = "__B_END_UNIQUE__"
    while sep_a in tokens_a or sep_a in tokens_b:
        sep_a += "_X"
    while sep_b in tokens_a or sep_b in tokens_b or sep_b == sep_a:
        sep_b += "_Y"

    concat = tokens_a + [sep_a] + tokens_b + [sep_b]
    sa = build_suffix_array(concat)
    lcp = build_lcp_array(concat, sa)

    len_a = len(tokens_a)
    len_b = len(tokens_b)
    dedup: set[tuple[int, int, int]] = set()

    for i in range(1, len(sa)):
        common_len = lcp[i]
        if common_len < min_match_len:
            continue
        s1 = sa[i - 1]
        s2 = sa[i]
        o1 = _origin_of_index(s1, len_a, len_b)
        o2 = _origin_of_index(s2, len_a, len_b)
        if o1 == -1 or o2 == -1 or o1 == o2:
            continue

        if o1 == 0:
            a_start = s1
            b_start = _to_local_index(s2, len_a)
        else:
            a_start = s2
            b_start = _to_local_index(s1, len_a)

        # Safety bounds.
        if a_start < 0 or b_start < 0:
            continue
        if a_start + common_len > len_a or b_start + common_len > len_b:
            common_len = min(len_a - a_start, len_b - b_start)
        if common_len < min_match_len:
            continue

        dedup.add((a_start, b_start, common_len))

    return [BakerMatch(a, b, l) for a, b, l in dedup]


def _select_non_overlapping(matches: list[BakerMatch], len_a: int, len_b: int) -> list[BakerMatch]:
    if not matches:
        return []
    selected: list[BakerMatch] = []
    cover_a = [False] * len_a
    cover_b = [False] * len_b

    for m in sorted(matches, key=lambda x: (-x.length, x.start_a, x.start_b)):
        ra = range(m.start_a, m.start_a + m.length)
        rb = range(m.start_b, m.start_b + m.length)
        if any(cover_a[i] for i in ra):
            continue
        if any(cover_b[j] for j in rb):
            continue
        selected.append(m)
        for i in ra:
            cover_a[i] = True
        for j in rb:
            cover_b[j] = True
    return selected


def baker_features_from_generalized_tokens(
    tokens_a: list[str],
    tokens_b: list[str],
    min_match_len: int = 3,
) -> dict[str, float]:
    len_a = len(tokens_a)
    len_b = len(tokens_b)
    if len_a == 0 or len_b == 0:
        return {
            "baker_similarity": 0.0,
            "baker_common_length": 0.0,
            "baker_longest_match": 0.0,
            "baker_num_matches": 0.0,
            "baker_coverage_a": 0.0,
            "baker_coverage_b": 0.0,
        }

    candidates = _extract_candidate_matches(tokens_a, tokens_b, min_match_len=min_match_len)
    selected = _select_non_overlapping(candidates, len_a=len_a, len_b=len_b)

    common_length = float(sum(m.length for m in selected))
    longest_match = float(max((m.length for m in selected), default=0))
    num_matches = float(len(selected))
    coverage_a = common_length / float(len_a) if len_a > 0 else 0.0
    coverage_b = common_length / float(len_b) if len_b > 0 else 0.0
    similarity = common_length / float(min(len_a, len_b)) if min(len_a, len_b) > 0 else 0.0

    return {
        "baker_similarity": similarity,
        "baker_common_length": common_length,
        "baker_longest_match": longest_match,
        "baker_num_matches": num_matches,
        "baker_coverage_a": coverage_a,
        "baker_coverage_b": coverage_b,
    }

