# https://vjudge.net/problem/UVA-10282
# Accepted

from sys import stdin


def load_dictionary(arr_num):
    dict_of_words[arr_num[1]] = arr_num[0]


def read_input(num):
    if(num in dict_of_words.keys()):
        print(dict_of_words[num])
    else:
        print("eh")


def main():
    load_dict = True
    for number in stdin:
        num = number.strip()
        if (num == ""):
            load_dict = False
        else:
            if (load_dict):
                # cargo el diccionario
                load_dictionary(num.split(" "))
            else:
                # leo entrada e imprimo resultado
                read_input(num)


dict_of_words = dict()
try:
    main()
except:
    pass
