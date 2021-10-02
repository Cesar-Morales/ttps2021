from sys import stdout, stdin

dictionary = dict()

numbers = stdin.readline().strip().split(" ")
for number in numbers:
    if(type(number) == int):
        if number in dictionary.keys():
            n = dictionary.get(number)
            dictionary[number] = n+1
        else:
            dictionary[number] = 1

for number in dictionary.keys():
    stdout.write("\r%s %s\n" % (number, dictionary.get(number)))
