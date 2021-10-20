# https://vjudge.net/problem/UVA-10192
# Runtime error

from sys import stdout, stdin
import numpy as np


def lcs(s, t):
    n = len(s) + 1
    m = len(t) + 1
    memo = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            if j == 0 or i == 0:
                pass
            elif s[i-1] == t[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    return memo[n-1][m-1]


def main():
    count = 1
    while True:
        set_c = stdin.readline().strip()
        if len(set_c) > 0 and set_c[0] == "#":
            break
        set_c2 = stdin.readline().strip()
        stdout.write("Case #{}: you can visit at most {} cities.\n".format(
            count, int(lcs(set_c, set_c2))))
        count += 1


main()
