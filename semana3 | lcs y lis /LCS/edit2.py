def ed(sA, sB):
    size_sA = len(sA)
    size_sB = len(sB)
    memo = [[0] * (size_sB + 1) for x in range(size_sA + 1)]
    for x in range(size_sA + 1):
        memo[x][0] = x
    for x in range(size_sB + 1):
        memo[0][x] = x
    for x in range(1, size_sA + 1):
        for y in range(1, size_sB + 1):
            memo[x][y] = min(
                memo[x - 1][y - 1] + (sA[x - 1] != sB[y - 1]),
                memo[x - 1][y] + 1,
                memo[x][y - 1] + 1)
    return memo[-1][-1]


def main():
    cant = int(input())
    for i in range(cant):
        stringA = input()
        stringB = input()
        print(ed(stringA, stringB))


main()  