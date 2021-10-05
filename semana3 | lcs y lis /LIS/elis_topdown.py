# https://vjudge.net/problem/SPOJ-ELIS

# TOP-DOWN

from sys import stdin, stdout


def lis(seq, idx):
    if (DP[idx] != -1):
        return DP[idx]
    DP[idx] = 1
    for i in range(idx):
        if((seq[i] < seq[idx]) and (DP[idx] < lis(seq, i)+1)):
            DP[idx] = lis(seq, i) + 1
    return DP[idx]


MAXN = int(stdin.readline().strip())
DP = [-1] * MAXN
seq = stdin.readline().strip().split(" ")
stdout.write(str(lis(seq, MAXN-1)))
