# https://vjudge.net/problem/UVA-10282

from sys import stdin


def load_dictionary():
    pass


def read_input():
    pass


def main():
    load_dict = True
    for number in stdin:
        num = number.strip()
        if (num == "0 0"):
            break
        if (num == ""):
            load_dict = False
        if (load_dict):
            # cargo el diccionario
            load_dictionary()
        else:
            # leo entrada e imprimo resultado
            read_input()


main()
