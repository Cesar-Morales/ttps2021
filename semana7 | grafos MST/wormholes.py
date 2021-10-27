# https://vjudge.net/problem/UVA-558

from sys import stdin, stdout

MAX = 9999999


def bellmanford(ady, anc):
    v = [MAX for _ in ady]
    v[0] = 0
    for i in range(len(ady)):
        possible = False
        for j in range(len(ady)):
            if v[j] == MAX:
                continue
            for u, w in zip(ady[j], anc[j]):
                if v[u] > v[j] + w:
                    possible = True
                    v[u] = v[j] + w
        if not possible:
            return False
    return True


test_cases = int(input())
for _ in range(test_cases):
    x, y = [int(x) for x in stdin.readline().strip().split()]
    adyacentes = [[] for _ in range(x)]
    ancho = [[] for _ in adyacentes]
    for _ in range(y):
        a, b, c = [int(x) for x in stdin.readline().strip().split()]
        adyacentes[a].append(b)
        ancho[a].append(c)
    stdout.writelines("possible\n") if bellmanford(
        adyacentes, ancho) else stdout.writelines("not possible\n")
