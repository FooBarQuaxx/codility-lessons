#!/usr/bin/env python


def solution(X, Y, D):
    return ( Y - X ) // D if ( Y - X ) % D == 0 else  ( Y - X ) // D + 1

print(solution(10, 85, 30))
