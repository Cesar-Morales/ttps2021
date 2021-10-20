# https://vjudge.net/problem/UVA-12455
# Bottom-Up

from sys import stdin
from functools import lru_cache

test_case = int(input())  # 0 ≤ t ≤ 50
for t in range(test_case):
    tamanio = int(input())  # 0 ≤ n ≤ 1000
    cantidad_barras = int(input())  # 1 ≤ p ≤ 20
    barras = list(map(int, stdin.readline().strip().split()))
    bool = False

    @lru_cache(maxsize=None)
    def mochila(cant, tam):
        # indice,capacidad
        if tam == 0:
            global bool
            bool = True
        if cant == -1:
            return 0
        elif barras[cant] > tamanio:
            return mochila(cant-1, tam)
        else:
            return max(mochila(cant-1, tam), mochila(cant-1, tam-barras[cant]) + barras[cant])

    mochila(cantidad_barras-1, tamanio)
    if bool:
        print("YES")
    else:
        print("NO")
