# https://vjudge.net/problem/UVA-11690

# Path compression
from sys import stdout

def find_set(x, f):
    if x != f[x]:
        f[x] = find_set(f[x], f)
    return f[x]

def unionByRank():
    r = find_set(frnd1, father)
    s = find_set(frnd2, father)
    if (s == r): return
    if rank[r] > rank[r]:
        father[s] = r
    elif rank[r] < rank[r]:
        father[r] = s
    else:
        father[r] = s
        rank[s] +=1


test_cases = int(input())

for case in range(test_cases):
    friends, remaining_friendships = [int(x) for x in input().split()]

    payments = []
    friendships = []
    for person in range(friends):
        payments.append(int(input()))
    for friend in range(remaining_friendships):
        person1, person2 = [int(x) for x in input().split()]
        friendships.append([person1, person2])

    # Create father and rank defaults
    # father[i] = padre del elemento i
    # rank similar o mayor a altura
    father = [x for x in range(friends)]  # c/u apunta a si mismo
    rank = [0 for x in range(friends)]   # arrancan de cero

    for each in friendships:
        frnd1 = each[0]
        frnd2 = each[1]

        unionByRank()

        debts = [0 for x in range(friends)]

        for i in range(friends):
            pad = find_set(i, father)
            debts[pad]+= payments[i]
        
        posible = True
        for s in debts:
            if s != 0:
                posible = False
                break
    
    stdout.write("POSSIBLE\n") if posible else stdout.write("IMPOSSIBLE\n")

# TEST CASE 
# 2
# 5 3
# 100
# -75
# -25
# -42
# 42
# 0 1
# 1 2
# 3 0
# 5 3
# 100
# -75
# -25
# -42
# 42
# 0 1
# 1 2
# 3 4

# imposible
# posible