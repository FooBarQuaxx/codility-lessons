#!/usr/bin/env python

def solution(A):
    from collections import Counter
    c = Counter(A)
    for k, v in c.items():
        if v % 2 == 1:
            return k


print(solution([9, 3, 9, 3, 9, 7, 9]))
