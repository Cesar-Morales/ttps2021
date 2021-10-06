# https://vjudge.net/problem/SPOJ-ELIS
# ACCEPTED

# TOP-DOWN

from sys import stdin, stdout


def lis(seq, idx):
    if (DP[idx] != -1):
        return DP[idx]
    DP[idx] = 1
    for i in range(idx):
        if((int(seq[i]) < int(seq[idx])) and (DP[idx] < lis(seq, i)+1)):
            DP[idx] = lis(seq, i) + 1
    return DP[idx]


def maxlis(idx):
    for i in range(idx):
        lis(seq, i)
    return str(max(DP))


MAXN = int(stdin.readline().strip())
DP = [-1] * MAXN
seq = stdin.readline().strip().split(" ")
stdout.write(maxlis(MAXN) + "\n")
