#!/usr/bin/env python


def solution(A):
    if len(A) == 0:
        return -1
    sum_left = sum(A[:0])
    sum_right = sum(A[1:])
    # print(sum_left, sum_right)
    if sum_left == sum_right:
        return 0
    for i in range(1, len(A)):
        sum_left += A[i-1]
        sum_right += -A[i]
        # print(sum_left, sum_right)
        if sum_left == sum_right:
            return i

    return -1
A = [-1, 3, -4, 5, 1, -6, 2, 1]
print(solution(A))

print(sum(A[:0]), sum(A[1:]))
print(sum(A[:1]), sum(A[2:]))
print(sum(A[:2]), sum(A[3:]))
print(sum(A[:3]), sum(A[4:]))
print(sum(A[:4]), sum(A[5:]))
print(sum(A[:5]), sum(A[6:]))
print(sum(A[:6]), sum(A[7:]))
# print(sum(A[:7]), sum(A[8:]))
