# https://vjudge.net/problem/UVA-11690

# Path compression
from sys import stdout

def find_set(x):
    if x != father[x]:
        father[x] = find_set(father[x])
    return father[x]

def unionByRank():
    r = find_set(frnd1)
    s = find_set(frnd2)
    if (s != r):
        if rank[r] > rank[s]:
            father[s] = r
        elif rank[r] < rank[s]:
            father[r] = s
        else:
            father[r] = s
            rank[s] +=1

test_cases = int(input())
result=[]
for case in range(test_cases):
    friends, remaining_friendships = [int(x) for x in input().split()]
    payments = []
    friendships = []
    for person in range(friends):
        payments.append(int(input()))
    for friend in range(remaining_friendships):
        person1, person2 = [int(x) for x in input().split()]
        friendships.append([person1, person2])
    father = [x for x in range(friends)]
    rank = [0]*friends
    for each in friendships:
        frnd1 = each[0]
        frnd2 = each[1]
        unionByRank()
        debts = [0]*friends
        for i in range(friends):
            pad = find_set(i)
            debts[pad]+= payments[i]
        posible = True
        for s in debts:
            if s != 0:
                posible = False
                break
    result.append(posible)
for r in result:
    stdout.write("POSSIBLE\n") if r else stdout.write("IMPOSSIBLE\n")

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