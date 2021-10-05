# https://vjudge.net/problem/SPOJ-ELIS

# Recursivo
# podemos pensarlo como lis(i) a la funcion que nos retorna la longitud de la subsecuencia mas largo que incluye a el elemento "i"
# muy costoso
# overlapping subproblems => si al hacer recursion se repiten subproblemas
# optimal substructure => si una solucion optima puede ser construida eficientemente a partir de otra solucion optima de sus subproblemas

from sys import stdin


def lis(idx):
    ans = 1
    for i in range(idx):
        if((seq[i] < seq[idx-1]) and (ans < lis(i)+1)):
            ans = lis(i) + 1
    return ans


size = int(stdin.readline().strip())
seq = stdin.readline().strip().split(" ")
print(lis(size))
