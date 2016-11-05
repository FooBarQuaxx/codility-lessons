#!/usr/bin/env python

def solution(N):
    # print(set(map(lambda x: len(x), [s for s in bin(N)[2:].split('1') if s != ''])))
    x = [s for s in bin(N)[2:].split('1')]
    if '0' in x[-1]:
        x = x[:-1]
    if '0' in x[0]:
        x  = x[1:]

    return max(set(map(lambda x: len(x), [s for s in x if s != ''])) or [0])


# print(solution(0))
# print(solution(9))
# print(solution(529))
# print(solution(50))
# print(solution(15))
# print(solution(1102))
print(solution(805306373))

# print(bin(110)[2:])
# print(bin(110)[2:].split('1'))
# import re
# print(re.split("(10)|(01)", bin(110)[2:]))
