# https://vjudge.net/problem/UVA-484
from sys import stdin

inputArr = [str(x) for x in stdin.readline().strip("\n").split(" ")]

setInputArr = set()

for num in inputArr:
    setInputArr.add(num)


for numIndex in inputArr:
    if (numIndex in setInputArr):
        print(numIndex, inputArr.count(numIndex))
        setInputArr.remove(numIndex)