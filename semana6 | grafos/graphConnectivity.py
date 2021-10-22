# https://vjudge.net/problem/UVA-459

import queue

def bfs(adj, ini, visit):
    q = queue.Queue()
    q.put(ini)
    while not q.empty():
        current = q.get()
        visit[current]=1
        for child in adj[current]:
            if not visit[child]:
                q.put(child)

