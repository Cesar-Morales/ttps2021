# https://vjudge.net/problem/UVA-10803

# N casos de prueba
# n ciudades (1 < n < 101)
# x,y localizacion [0, 1023]
# no funciona

from sys import stdout, stdin
import math
import numpy as np

INF = 9999999666666666


def dist(i, j):
    return math.sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]))


x = []
y = []
test_case = int(stdin.readline())
for _ in range(test_case):

    cities = int(stdin.readline())
    adjMat = np.ones((cities, cities), dtype=int)

    for i in range(cities):
        a, b = [int(x) for x in stdin.readline().strip().split()]
        x.append(a)
        y.append(b)
    for i in range(cities):
        for j in range(cities):
            adjMat[i][j] = dist(i, j)
            if(adjMat[i][j] > 10):
                adjMat[i][j] = INF

    for k in range(cities):
        for i in range(cities):
            for j in range(cities):
                if adjMat[i][j] > adjMat[i][k] + adjMat[k][j]:
                    adjMat[i][j] = adjMat[i][k] + adjMat[k][j]
    print(adjMat)
    max = 0
    for i in range(cities):
        for j in range(cities):
            if(adjMat[i][j] > max):
                max = adjMat[i][j]
    if max == INF:
        stdout.writelines("send")
    else:
        stdout.writelines(str(max))
    stdout.writelines("\n")
