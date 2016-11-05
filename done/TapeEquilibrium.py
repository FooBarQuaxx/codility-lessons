#!/usr/bin/env python


def solution(A):
    _s = set()
    sum_left = sum(A[:1])
    sum_right = sum(A[1:])
    print(sum_left, sum_right)
    _s.add(abs(sum_left - sum_right))
    for i in range(1, len(A)-1):
        sum_left += A[i]
        sum_right -= A[i]
        _s.add(abs(sum_left - sum_right))

    return min(_s)

print(solution([-1000, 1000]))
print(solution([3, 1, 2, 4, 3]))
