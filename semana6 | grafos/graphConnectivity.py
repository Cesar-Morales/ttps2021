# https://vjudge.net/problem/UVA-459

# QUEUE
# push = put
# pop = get
# queue.Queue() constructor fifo queue
# edges = aristas = puentes
# ACCEPTED

import queue


def bfs(v, visitados):
    cola = queue.Queue()
    cola.put(v)
    while not cola.empty():
        t = cola.get()
        visitados[t] = 1
        for w in adyacentes[t]:
            if not visitados[w]:
                cola.put(w)


def cc():
    numCC = 0
    visitados = [0 for x in adyacentes]
    vertice = 0
    while True:
        numCC += 1
        bfs(vertice, visitados)
        try:
            vertice = visitados.index(0)
        except:
            break
    return numCC


def addEdge(u, w):
    adyacentes[u].append(w)
    adyacentes[w].append(u)


min = ord("A")
test_cases = int(input())
input()
for case in range(test_cases):
    max = ord(input())-min+1
    adyacentes = [[] for x in range(max)]
    edge = input()
    while edge:
        a, b = [ord(i)-min for i in list(edge)]
        addEdge(a, b)
        try:
            edge = input()
        except:
            break
    print(cc())
    if test_cases-case > 1:
        print()
