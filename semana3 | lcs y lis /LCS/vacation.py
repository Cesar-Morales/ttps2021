# https://vjudge.net/problem/UVA-10192

case_counter = 1
while True:
    set_of_cities = input()
    if len(set_of_cities) > 0 and set_of_cities[0] == "#":
        break
    set_of_cities2 = input()
    if len(set_of_cities2) > 0 and set_of_cities2[0] == "#":
        break
    count_c = len(set_of_cities) + len(set_of_cities2)
    print("Case #{}: you can visit at most {} cities.".format(case_counter, count_c))
    case_counter += 1
