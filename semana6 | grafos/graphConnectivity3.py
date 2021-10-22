# https://vjudge.net/problem/UVA-459

# QUEUE
# push = put
# pop = get
# queue.Queue() constructor fifo queue
# edges = aristas = puentes


import sys


def dfs(u):
    visitado[u] = True
    for w in adyacentes[u]:
        if not visitado[w]:
            dfs(w)


def addEdge(u, w):
    adyacentes[u].append(w)
    adyacentes[w].append(u)


test_cases = int(input())
input()
min = ord("A")
for case in range(test_cases):
    max = ord(input())+1-min
    adyacentes = [[] for x in range(max)]
    visitado = [False for x in range(max)]
    cnt = 0
    edge = input()
    while edge != "":
        a, b = [ord(i)-min for i in list(edge)]
        addEdge(a, b)
        edge = input()
    for i in range(max):
        if (not visitado[i]):
            dfs(i)
            cnt += 1
    print(cnt)
    if test_cases-case > 1:
        print()
