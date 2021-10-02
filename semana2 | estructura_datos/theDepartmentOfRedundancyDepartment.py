# https://vjudge.net/problem/UVA-484


from sys import stdin, stdout

dictionary = dict()

num_arr = stdin.readline().strip().split(" ")
try:
    for num in num_arr:
        if(num in dictionary.keys()):
            cantAux = dictionary.get(num)
            cantAux += 1
            dictionary.update({num: cantAux})
        else:
            if(type(int(num)) == int):
                dictionary[num] = 1
except:
    pass
for n in dictionary.keys():
    stdout.write("%s %s\n" % (n, dictionary[n]))
