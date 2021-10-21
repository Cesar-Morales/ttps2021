# https://vjudge.net/problem/UVA-10583

# cada caso comienza con:
# n (estudiantes) y m (casos)
# continua con m pares
# i y j
# 0 0 final
from sys import stdin, stdout

def find_set(x):
    if x != p[x-1]:
        p[x-1] = find_set(p[x-1])
    return p[x-1]

def unionByRank(x, y):
    r = find_set(x)
    s = find_set(y)
    if (s != r):
        if rank[r-1] > rank[s-1]:
            p[s-1] = r
        elif rank[r-1] < rank[s]:
            p[r-1] = s
        else:
            p[r-1] = s
            rank[s-1] +=1

index = 1
while True:
    tree = []
    n, m = [int(x) for x in stdin.readline().split()]
    if n==0 and m == 0:
        break
    for each in range(m):
        i, j = [int(x) for x in stdin.readline().split()]
        tree.append([i,j])
    p = [x+1 for x in range(n)]
    rank = [0]*n
    for node in tree:
        unionByRank(node[0], node[1])
    stdout.write("Case %d: %d\n" % (index,len(set(p))))
    index += 1