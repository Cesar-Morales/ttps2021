# https://vjudge.net/problem/UVA-10192


def LCS(s, t):
    n = len(s) + 1
    m = len(t) + 1
    for i in range(n):
        memo.append([-1]*m)

    for i in range(n):
        memo[i][0] = 0
    for j in range(m):
        memo[0][j] = 0

    for i in range(n):
        for j in range(m):
            if j == 0 or i == 0:
                pass
            elif s[i-1] == t[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    return memo[n-1][m-1]


def main():
    case_counter = 1
    while True:
        set_of_cities = input()
        if len(set_of_cities) > 0 and set_of_cities[0] == "#":
            break
        set_of_cities2 = input()
        if len(set_of_cities2) > 0 and set_of_cities2[0] == "#":
            break
        count_c = LCS(set_of_cities, set_of_cities2)
        print("Case #{}: you can visit at most {} cities.".format(
            case_counter, count_c))
        case_counter += 1


memo = []
main()
