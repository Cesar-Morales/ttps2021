# https://vjudge.net/problem/UVA-11690

# Path compression


def find_set(x, f):
    if x != f[x]:
        f[x] = find_set(f[x], f)
    return f[x]


test_cases = int(input())

for case in range(test_cases):
    friends, remaining_friendships = [int(x) for x in input().split()]
    #print("n = ", n)
    #print("m = ", m)
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
    father = [x for x in friends]  # c/u apunta a si mismo
    rank = [0 for x in friends]   # arrancan de cero

    for each in friendships:
        frnd1 = each[0]
        frnd2 = each[1]
        r = find_set(frnd1, father)
        s = find_set(frnd2, father)
        if (s != r):

            # TEST CASE 1
            # 5 3
            # 100
            # -75
            # -25
            # -42
            # 42
            # 0 1
            # 1 2
            # 3 4
