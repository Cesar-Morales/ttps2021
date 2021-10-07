

memo = []


def LCS(s, t):
    n = len(s) + 1
    m = len(t) + 1
    for i in range(n):
        memo.append([-9999]*m)

    for i in range(n):
        memo[i][0] = 0
    for j in range(m):
        memo[0][j] = 0

    for f in range(n):
        for c in range(m):
            print("\t", memo[f][c], end=" ")
        print()
    """for i in n:
        for j in m:
            if s[i-1] == t[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    return memo[n-1][m-1]"""


#   columna, fila
LCS("HOLA", "chauchau")
