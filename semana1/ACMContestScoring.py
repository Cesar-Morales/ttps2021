# ACM Contest Scoring = https://vjudge.net/problem/Kattis-acm

from sys import stdin
  
# Salvo todo en un arreglo de listas
numsArr = []  
aux = stdin.readline()  
while (aux[:-1] != "-1"):
    numsArr.append(aux[:-1].split(" "))
    aux = stdin.readline()

# Guardo datos particulares en diccionarios

for n in numsArr:
  print (n[0])