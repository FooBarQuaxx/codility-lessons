#!/usr/bin/env python

from collections import Counter
def solution(A):
    if min(A) != 1:
        return 0
    if max(A) != len(A):
        return 0
    c1 = Counter(A)
    c2 = Counter(range(1, len(A) + 1))
    return 1 if c1 == c2 else 0

import pytest
@pytest.mark.parametrize("A, expected", [
    ([4, 1, 3, 2], 1),
    ([4, 1, 3],    0),
    ([1],    1),
])
def test_solution(A, expected):
    assert solution(A) == expected
