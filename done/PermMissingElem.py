#!/usr/bin/env python


def solution(A):
    from collections import Counter
    if len(A) == 0:
        return 1
    c1 = Counter({v:1 for v in range(1, len(A) + 2)})
    c2 = Counter({v:-1 for v in A})
    c3 = c1 + c2
    # print(c1)
    # print(c2)
    # print(c3)
    most_common = c3.most_common()
    if most_common:
        return most_common[-1][0]
    else:
        return 1


# print(solution([2, 3, 1, 5]))
# print(solution([]))
# print(solution([2]))
# print(solution([1]))
# print(solution([1,3]))
