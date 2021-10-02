from sys import stdin, stdout
list_num = list(map(int, stdin.readline().strip().split()))
while len(list_num) != 0:
    num = list_num[0]
    count = list_num.count(num)
    for i in range(count):
        list_num.remove(num)
    stdout.write("{} {}".format(num, count))
    print()

#      3 1 2 2 1 3 5 3 3 2
