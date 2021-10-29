# https://vjudge.net/problem/SPOJ-EDIST
# 
#import time
from functools import lru_cache
from sys import stdin, stdout

def main():
    cant = int(stdin.readline().strip())
    for _ in range(cant):
        strA = stdin.readline().strip()
        strB = stdin.readline().strip()
        @lru_cache
        def DP(i, j):
            if (j == 0):
                return i
            elif(i == 0):
                return j
            elif (strA[i - 1] == strB[j - 1]):
                return DP(i - 1, j - 1)
            return 1 + min(DP((i - 1), j), 
                        DP(i, j - 1), 
                        DP(i-1, j-1))
        stdout.write("{}\n".format(DP(len(strA),len(strB))))
    return 0
main()
#print(time.time()) 