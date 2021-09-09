from sys import stdin
AUX = -999

## Ingreso de datos
try:
    numsArr = [int(x) for x in stdin.readline().split(" ")]
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
                raise Exception()
        # 5 1 4 2 -1 6
        print("Jolly")
except:
    print("Not jolly")