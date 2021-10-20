# https://vjudge.net/problem/UVA-10192
# Accepted

from sys import stdout
from functools import lru_cache

count = 1
while True:
    set_c = input()
    if set_c == "#":
        break
    set_c2 = input()
    n = len(set_c)
    m = len(set_c2)

    @lru_cache(maxsize=None)
    def memo(i, j):
        if i == n or j == m:
            return 0
        elif set_c[i] == set_c2[j]:
            return memo(i+1, j+1) + 1
        else:
            return max(memo(i+1, j), memo(i, j+1))

    result_lcs = memo(0, 0)
    stdout.write("Case #{}: you can visit at most {} cities.\n".format(
        count, result_lcs))
    count += 1
