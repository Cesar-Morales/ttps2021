# https://vjudge.net/problem/UVA-484
from sys import stdin

inputArr = [str(x) for x in stdin.readline().strip("\n").split(" ")]

setInputArr = set(inputArr)

for numIndex in setInputArr:
    print(numIndex, inputArr.count(numIndex))