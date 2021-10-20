

def crear_matriz(n, m):
    for i in range(n):
        matriz.append([-1]*m)


def imprimir_matriz(n, m):
    print("\t", "x", end=" ")
    for i in range(m):
        print("\t", "c{}".format(i), end=" ")
    print()
    for f in range(n):
        for c in range(m):
            if c == 0:
                print("\t", "f{}".format(f), end=" ")
            print("\t", matriz[f][c], end=" ")
        print()


def main():
    print("Ingrese filas: ")
    n = int(input())
    print("Ingrese columnas: ")
    m = int(input())
    crear_matriz(n, m)
    imprimir_matriz(n, m)


matriz = []

main()
