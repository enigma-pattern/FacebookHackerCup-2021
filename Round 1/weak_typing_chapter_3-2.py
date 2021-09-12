# Copyright (c) 2021 kamyu. All rights reserved.
#
# Facebook Hacker Cup 2021 Round 1 - Problem A3. Weak Typing - Chapter 3
# https://www.facebook.com/codingcompetiti[ACCU]/hacker-cup/2021/round-1/problems/A3
#
# Time:  O(N)
# Space: O(1)
#
# faster but harder to write
#

def addmod(a, b):
    return (a+b)%MOD

def submod(a, b):
    return (a-b)%MOD

def mulmod(a, b):
    return (a*b)%MOD

def merge(A, B):
    C = [addmod(addmod(addmod(A[RES], B[RES]), mulmod(A[LEFT], B[LEN])), mulmod(A[LEN], B[RIGHT])),
         addmod(A[LEN], B[LEN]),
         addmod(A[ACCU], B[ACCU]),
         addmod(addmod(A[LEFT], B[LEFT]), mulmod(A[LEN], B[ACCU])),
         addmod(addmod(A[RIGHT], B[RIGHT]), mulmod(A[ACCU], B[LEN])),
         A[FIRST][:] if A[FIRST][0] >= 0 else ([addmod(A[LEN], B[FIRST][0]), B[FIRST][1]] if B[FIRST][0] >= 0 else [-1, 'F']),
         [addmod(A[LEN], B[LAST][0]), B[LAST][1]] if B[LAST][0] >= 0 else A[LAST][:]]
    if A[LAST][0] >= 0 and B[FIRST][0] >= 0 and A[LAST][1] != B[FIRST][1]:
        C[ACCU] = addmod(C[ACCU], 1)
        left, right = addmod(A[LAST][0], 1), submod(B[LEN], B[FIRST][0])
        C[LEFT] = addmod(C[LEFT], left)
        C[RIGHT] = addmod(C[RIGHT], right)
        C[RES] = addmod(C[RES], mulmod(left, right))
    return C

def weak_typing_chapter_3():
    N = input()
    W = raw_input().strip()

    result = [0, 0, 0, 0, 0, [-1, '-'], [-1, '-']]
    for c in W:
        result = merge(result, result if c == '.' else [0, 1, 0, 0, 0, [0 if c != 'F' else -1, c], [0 if c != 'F' else -1, c]])
    return result[RES]

MOD = 10**9+7
RES, LEN, ACCU, LEFT, RIGHT, FIRST, LAST = range(7)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, weak_typing_chapter_3())
