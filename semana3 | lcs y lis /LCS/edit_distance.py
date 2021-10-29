# https://vjudge.net/problem/SPOJ-EDIST

from functools import lru_cache
from sys import stdin, stdout

cant = stdin.readline()
for _ in range(int(cant)):
    strA = stdin.readline().strip()
    strB = stdin.readline().strip()

    @lru_cache(maxsize=None)
    def DP(i, j):
        if (j == 0):
            return i
        elif(i == 0):
            return j
        return min(DP((i - 1), j)+1,
                   DP(i, j - 1)+1,
                   DP(i-1, j-1) + (1 if (strA[i-1] != strB[j-1]) else 0))
    stdout.write("{}\n".format(DP(len(strA), len(strB))))
