from sys import stdin
for line in stdin:
    if line[0] == '#':
        break
    print(line)
