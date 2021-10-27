# https://vjudge.net/problem/SPOJ-EDIST

from functools import lru_cache
from sys import stdin, stdout
import re

def sacarIguales(sA,sB):
    for eachChar in sA:
        if(eachChar in sB):
            sB = re.sub(eachChar,"",sB , count = 1)
            sA = re.sub(eachChar,"",sA , count = 1)
    return sA, sB



cant = int(stdin.readline())
for _ in range(cant):
    stringA = input()
    stringB = input()
    @lru_cache()
    def DP(i, j):
        if (j == 0):
            return i
        elif(i == 0):
            return j
        elif (stringA[i - 1] == stringB[j - 1]):
            return DP(i - 1, j - 1)
        return 1 + min( DP((i - 1), j), 
                        DP(i, j - 1), 
                        DP(i-1, j-1))
    stdout.write(str(DP(len(stringA),len(stringB)))+"\n")
