# ACM Contest Scoring = https://vjudge.net/problem/Kattis-acm

from sys import stdin
  
# Salvo todo en un arreglo de listas
diccionarioDeDatos = dict()  
ultimoLeido = stdin.readline()  
while (ultimoLeido[:-1] != "-1"):
    ultimosDatosLista = ultimoLeido[:-1].split(" ")
    if(ultimosDatosLista[1] in diccionarioDeDatos.keys()):
        if("right" not in diccionarioDeDatos[ultimosDatosLista[1]]): 
            diccionarioDeDatos[ultimosDatosLista[1]]= diccionarioDeDatos[ultimosDatosLista[1]] + [ultimosDatosLista[0],ultimosDatosLista[2]]
    else:
        diccionarioDeDatos[ultimosDatosLista[1]]=[ultimosDatosLista[0],ultimosDatosLista[2]]
    ultimoLeido = stdin.readline()

# Guardo datos particulares en diccionarios
ok = 0
tot = 0
for key in diccionarioDeDatos.keys():
    # resultados tiene guardado todos los resultados de la clave
    resultados = diccionarioDeDatos[key][1::2]
    totAux = 0
    if("right" in resultados):
        # tiempos tiene guardado todos los resultados del tiempo
        tiempoPorIntentos = diccionarioDeDatos[key][0::2]
        totAux += ((len(tiempoPorIntentos))-1)*20
        totAux += int(diccionarioDeDatos[key][-2])
        ok+=1
        tot+=totAux
print(ok, " ", tot)


# INPUT
# 3 E right
# 10 A wrong
# 30 C wrong
# 50 B wrong
# 100 A wrong
# 200 A right
# 250 C wrong
# 300 D right
# -1

# OUTPUT
# 3 543