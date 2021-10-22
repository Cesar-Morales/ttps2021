# https://vjudge.net/problem/UVA-796
# ACCEPTED

from sys import stdout, stdin

# no dirigido


def addEdge(u, w):
    adyacentes[u].append(w)
    adyacentes[w].append(u)


def search_bridge(v):
    global cnt
    visitados[v] = 1
    df_number[v] = cnt
    cnt += 1
    low[v] = df_number[v]
    for w in adyacentes[v]:
        if visitados[w] == 0:
            p[w] = v
            search_bridge(w)
            if low[w] > df_number[v]:
                bridges.append((min(v, w), max(v, w)))
            low[v] = min(low[v], low[w])
        elif p[v] != w:
            low[v] = min(low[v], df_number[w])


# main
for line in stdin:
    if(line == "\n"):
        break
    n_servs = int(line)
    if (n_servs != 0):
        adyacentes = [[] for _ in range(n_servs)]
        for s in range(n_servs):
            links = stdin.readline().strip().split()
            for i in range(int(links[1][1])):
                addEdge(int(links[0]), int(links[i+2]))
        visitados = [0 for _ in range(n_servs)]
        p = [int(x) for x in range(n_servs)]
        df_number = [0 for _ in range(n_servs)]
        low = [0 for _ in range(n_servs)]
        bridges = []
        cnt = 1
        for v in range(n_servs):
            if visitados[v] == 0:
                search_bridge(v)
        stdout.write(str(len(bridges))+" critical links\n")
        bridges = sorted(bridges, key=lambda x: (x[0], x[1]))
        for elem in bridges:
            stdout.write(str(elem[0])+" - "+str(elem[1])+"\n")
        input()
    else:
        stdout.write("0 critical links\n")
    stdout.write("\n")
    stdin.readline()


#   0 (1) 1
#   1 (3) 2 0 3
#   2 (2) 1 3
#   3 (3) 1 2 4
#   4 (1) 3
#   7 (1) 6
#   6 (1) 7
#   5 (0)
#   0
