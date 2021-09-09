from sys import stdin, stdout
 
## Ingreso de datos

numsArr = [int(x) for x in stdin.readline().split(" ")]
numsArr = [ elemento for elemento in numsArr if elemento != "" ]
## Obtener elementos
setNums = set()
arrSize = len(numsArr)
for i in range(1, arrSize):
    setNums.add(i)

## TEST
for index in range(0, len(setNums)):
    num = int(numsArr[index])
    nextNum = int(numsArr[index + 1])
    diff = abs(num - nextNum)
    if(diff in setNums):
        setNums.remove(diff)
if (len(setNums) == 0):
    stdout.write("Jolly")
else:
    stdout.write("Not jolly")
    
    