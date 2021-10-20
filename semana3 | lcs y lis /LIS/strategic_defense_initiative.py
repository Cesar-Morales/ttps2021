# https://vjudge.net/problem/UVA-497

# bottom-up

from sys import stdout


def lis(seq):
    ans = 0

    for i in range(len(seq)):
        DP[i] = 1
        prev[i] = -1
        for j in range(i):
            if seq[j] < seq[i] and DP[i] < DP[j] + 1:
                DP[i] = DP[j]+1
                prev[i] = j

        if (DP[ans] < DP[i]):
            ans = i
    return ans


def imprimir_inverso(actual):
    l = []
    l.append(int(seq[actual]))
    prox = prev[actual]
    while prox != -1:
        l.append(int(seq[prox]))
        prox = prev[prox]
    return sorted(l)


num_test_case = int(input())
input()
for i in range(num_test_case):
    seq = []
    while True:
        n = input()
        if n == "":
            break
        seq.append(int(n))
    DP = [-1] * len(seq)
    prev = [-1] * len(seq)
    MAXN = lis(seq)
    stdout.write("Max hits: {}\n".format(DP[MAXN]))
    for i in imprimir_inverso(MAXN):
        print(i)
    stdout.write("\n")
