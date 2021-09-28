# https://vjudge.net/problem/UVA-484
from sys import stdin, stdout

numArr = [str(x) for x in stdin.readline().strip().split(" ")]
number_set = set()
dictionary = dict()

for num in numArr:
    if(num in number_set):
        cantAux = dictionary.get(num)
        dictionary.update({num:cantAux})
    else:
        number_set.add(num)
        dictionary.update({num:1})

for n in number_set:
    stdout.write("\r%s %s\n" % (n, numArr.count(n)))