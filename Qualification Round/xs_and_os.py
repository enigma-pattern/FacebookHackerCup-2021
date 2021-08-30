# Copyright (c) 2021 kamyu. All rights reserved.
#
# Facebook Hacker Cup 2021 Qualification Round - Problem B. Xs and Os
# https://www.facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/B
#
# Time:  O(N^2)
# Space: O(1)
#
    
def number_of_sets(C, cnt):
    result = sum(int(sum(1 if C[i][j] == '.' else (float("inf") if C[i][j] == 'O' else 0) for j in xrange(len(C[0]))) == cnt) for i in xrange(len(C)))
    result += sum(int(sum(1 if C[i][j] == '.' else (float("inf") if C[i][j] == 'O' else 0) for i in xrange(len(C))) == cnt) for j in xrange(len(C[0])))
    if cnt == 1:
        for i in xrange(len(C)):
            if sum(1 if C[i][j] == '.' else (float("inf") if C[i][j] == 'O' else 0) for j in xrange(len(C[0]))) != 1:
                continue
            j = C[i].index('.')
            if sum(1 if C[k][j] == '.' else (float("inf") if C[k][j] == 'O' else 0) for k in xrange(len(C))) == 1:
                result -= 1
    return result

def xs_and_os():
    N = input()
    C = [raw_input().strip() for _ in xrange(N)]

    cnt = min(min(sum(1 if C[i][j] == '.' else (float("inf") if C[i][j] == 'O' else 0) for j in xrange(N)) for i in xrange(N)),
              min(sum(1 if C[i][j] == '.' else (float("inf") if C[i][j] == 'O' else 0) for i in xrange(N)) for j in xrange(N)))
    return "%s %s" % (cnt, number_of_sets(C, cnt)) if cnt != float("inf") else "Impossible"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, xs_and_os())
