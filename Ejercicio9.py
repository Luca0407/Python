"""
9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por
ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""
def generar_n_caracteres(n, val):
    for i in range(n):
        print(val, end="")


caracter = input("¿Qué caracter quiere imprimir?\n")
cantidad = int(input("¿Cuántas veces quiere imprimirlo?\n"))

generar_n_caracteres(cantidad, caracter)
