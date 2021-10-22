# https://vjudge.net/problem/UVA-459

# QUEUE
# push = put
# pop = get
# queue.Queue() constructor fifo queue
# edges = aristas = puentes

import queue


def bfs(v, visitados):
    cola = queue.Queue()
    cola.put(v)
    while not cola.empty():
        t = cola.get()
        for w in adyacentes[t]:
            if not visitados[w]:
                cola.put(w)
                visitados[w] = 1


def cc():
    numCC = 0
    visitados = [0 for x in adyacentes]
    for vertice in range(len(adyacentes)):
        if (visitados[vertice] == 0):
            numCC += 1
            bfs(vertice, visitados)
    return numCC


test_cases = int(input())
input()
min = ord("A")
for case in range(test_cases):
    max = ord(input())+1-min
    adyacentes = [[] for x in range(max)]
    edge = input()
    while edge != "":
        a, b = [ord(i)-min for i in list(edge)]
        adyacentes[a].append(b)
        adyacentes[b].append(a)
        edge = input()
    print(cc())
