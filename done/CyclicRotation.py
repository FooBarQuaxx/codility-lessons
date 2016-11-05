#!/usr/bin/env python


def solution(N, K):
    from collections import deque
    d = deque(N)
    d.rotate(K)
    return list(d)
