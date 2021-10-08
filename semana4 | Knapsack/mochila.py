def mochila():
    for i in range(n):
        DP[i][0] = 0
    for j in range(k):
        DP[0][j] = 0
    for i in range(n):
        for j in range(k):
            if elem[i-1][0] > j:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i-1]
                               [j-elem[i-1][0]] + elem[i-1][1])
    return DP[n][k]


k = 9   # peso maximo que soporta la mochila
n = int(input())     # cantidad elementos

elem = []
for i in range(n):
    peso = int(input())
    costo = int(input())
    elem.append((peso, costo))
print(elem)
DP = []
# print(mochila())  NO FUNCIONA
