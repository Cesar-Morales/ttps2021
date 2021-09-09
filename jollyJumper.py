#Jolly Jumper = https://vjudge.net/problem/UVA-10038

from sys import stdin
AUX = -999

## Ingreso de datos
try:
    numsArr = [int(x) for x in stdin.readline().split(" ")]
    numsArr = [ elemento for elemento in numsArr if elemento != "" ]
    ## Obtener resultados
    aux = AUX
    resNumArr = []
    for num in numsArr:
        if (aux == AUX):
            aux = abs(int(num))
        else:
            numAux = abs(int(num))
            resNumArr.append(abs(aux - numAux))
            aux = numAux
            
    ## TEST
    
    resNumArr= sorted(resNumArr, reverse=True)
    n = len(numsArr)
    nRes = len(resNumArr)

    if(n == 1):
        print("Jolly")
    else:
        for index, seq in enumerate(resNumArr):
            if (seq != n - (index + 1)):
                # 4 1 4 2 3
                # 3 5 8 4
                raise
        # 5 1 4 2 -1 6
        # 1 10 2 9 3 8 4 7 5 6
        print("Jolly")
except:
    print("Not jolly")