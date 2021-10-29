# https://vjudge.net/problem/SPOJ-EDIST
# 
import time
from sys import stdin, stdout
import numpy as np

def ed():
    n= len(s)+1
    m= len(t)+1
    memo = np.zeros((n,m), dtype=int)
    for i in range(n): memo[i][0] = i
    for j in range(m): memo[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            memo[i][j] = memo[i-1][j-1] + (1 if (s[i-1] != t[j-1]) else 0)
            memo[i][j] = min(memo[i][j], memo[i-1][j] + 1)
            memo[i][j] = min(memo[i][j], memo[i][j-1] + 1)
    return memo[i-1][j-1]

cant = int(stdin.readline())
for _ in range(cant):
    s = stdin.readline()
    t = stdin.readline()
    max = ed()
    stdout.write("{}\n".format(max))

print(time.time())