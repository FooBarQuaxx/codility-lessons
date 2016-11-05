#!/usr/bin/env python

def solution(A, X):
    the_set = set(range(1, X+1))
    s = set()
    for i in xrange(len(A)):
        s.add(A[i])
        if s == the_set:
            return i
    return -1 



import pytest
@pytest.mark.parametrize("A, X, expected", [
    ([ 1, 3, 1, 4, 2, 3, 5, 4 ], 5, 6),
    ([ 1 ], 1, 0),
    ([ 1 ], 2, -1),
    ([ 2 , 1], 2, 1),
])
def test_solution(A, X, expected):
    assert solution(A, X) == expected

# print(solution([ 1, 3, 1, 4, 2, 3, 5, 4 ], 5))
