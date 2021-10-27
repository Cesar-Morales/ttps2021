# https://vjudge.net/problem/UVA-459

# QUEUE
# push = put
# pop = get
# queue.Queue() constructor fifo queue
# edges = aristas = puentes

import queue


def bfs(adjacency, start, visited):
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        current = q.get()
        visited[current] = 1
        for child in adjacency[current]:
            if not visited[child]:
                q.put(child)


def cc(adjacency):
    components = 0
    visited = [0 for x in adjacency]
    index = 0
    while True:
        bfs(adjacency, index, visited)
        components += 1
        try:
            index = visited.index(0)
        except:
            break
    return components


test_cases = int(input())
input()
min = ord("A")
for case in range(test_cases):
    n = (ord(input())-min)+1
    adjacency = [[] for x in range(n)]
    conn = input()
    while conn:
        a, b = [ord(i)-min for i in list(conn)]
        adjacency[a].append(b)
        adjacency[b].append(a)

    print(cc(adjacency))
    if test_cases-case > 1:
        print()
