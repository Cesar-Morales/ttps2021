from sys import stdin, stdout

freq_map = {}
numbers_list = list()

numbers = list(map(int, stdin.readline().strip().split()))

for number in numbers:
    if number in freq_map:
        freq_map[number] += 1
    else:
        freq_map[number] = 1
        numbers_list.append(number)

for number in numbers_list:
    stdout.write("%s %s\n" % (number, freq_map[number]))

#      3 1 2 2 1 3 5 3 3 2
