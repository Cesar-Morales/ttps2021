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
print(diccionarioDeDatos.keys())
print(diccionarioDeDatos.values())
print(diccionarioDeDatos["B"][0::2])
lista = diccionarioDeDatos["B"][0::2]

# Probando una suma
tot = (len(lista)-1)*20
for index, num in enumerate(lista):
    tot+=int(num)
print(tot)


