

memo = []


def imprimir_matriz(n, m, s, t):
    print("\t", "-----DEBUG MATRIZ-----")
    print("\t", "x", end=" ")
    for i in range(m):
        if(i == 0):
            print("\t", "NULL", end=" ")
        else:
            print("\t", "{}".format(t[i-1]), end=" ")
    print()
    for i in range(n):
        for j in range(m):
            if j == 0 and i == 0:
                print("\t", "NULL", end=" ")
            elif j == 0:
                print("\t", "{}".format(s[i-1]), end=" ")
            print("\t", memo[i][j], end=" ")
        print()
    print()


def LCS(s, t):
    n = len(s) + 1
    m = len(t) + 1
    for i in range(n):
        memo.append([-1]*m)

    for i in range(n):
        memo[i][0] = 0
    for j in range(m):
        memo[0][j] = 0

    #imprimir_matriz(s, t)

    for i in range(n):
        for j in range(m):
            if s[i-1] == t[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    imprimir_matriz(n, m, s, t)
    return memo[n-1][m-1]


set_of_cities = input()
set_of_cities2 = input()
print(LCS(set_of_cities, set_of_cities2))
