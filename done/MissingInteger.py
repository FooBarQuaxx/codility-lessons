#!/usr/bin/env python


from pprint import pprint as pp
from collections import Counter

def solution(A):
    max_of_a = max(A)
    if max_of_a <= 0:
        return 1
    if max_of_a == 1:
        return 2
    s = set(A)
    for x in xrange(1, max_of_a):
        if x not in s:
            return x
    return max_of_a + 1
    # return 1
    # c1 = Counter({v:1 for v in range(1, max_of_a + 2)})
    # c2 = Counter({v:-1 for v in A})
    # pp(c1)
    # pp(c2)
    # return list((c1 + c2).elements())[0]

import pytest
@pytest.mark.parametrize("A, expected", [
    ([ 1, 3, 6, 4, 1, 2 ], 5),
    ([0],    1),
    ([-2147483648, 2147483648],    1),
    ([1],    2),
    ([2],    1),
    ([3],    1),
    ([-1],    1),
    (list(xrange(1, 10000001)), 10000001)
])
def test_solution(A, expected):
    assert solution(A) == expected
