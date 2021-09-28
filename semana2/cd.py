# https://vjudge.net/problem/UVA-11849

from sys import stdin
while True:
    try:
        number = stdin.readline().strip().split(' ')
        print(number)
    except:
        break
"""
load_dict = True
    for number in stdin:
        num = number.strip()
        if (num == "fin"):
            break
        if (num == ""):
            load_dict = False
        else:
            if (load_dict):
                # cargo el diccionario
                load_dictionary(num.split(" "))
            else:
                # leo entrada e imprimo resultado
                read_input(num)
"""
