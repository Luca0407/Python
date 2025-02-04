"""
10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
"""
numeros = []


def histograma(lista):
    for i in lista:
        print("*" * i, end="")
        print("")


while True:
    num = int(input("introduzca un número a la lista\nEscriba '0' para finalizar\n"))
    if num != 0:
        numeros.append(num)
    else:
        break


histograma(numeros)
