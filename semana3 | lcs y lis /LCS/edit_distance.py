# https://vjudge.net/problem/SPOJ-EDIST

from functools import lru_cache


def main():
    cant = int(input())
    for i in range(cant):
        stringA = input()
        stringB = input()

        @lru_cache(maxsize=None)
        def DP(i, j):
            if (j == 0):
                return i
            elif(i == 0):
                return j
            else:
                return min(DP((i - 1), j), DP(i, j - 1), DP((i - 1), (j - 1)))

       print(DP(0,0))


main()
