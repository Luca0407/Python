"""
8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o
devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""
lista1 = []
lista2 = []


def superposicion(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
            else:
                continue
    return False


while True:
    palabras = input("Ingrese palabras a la lista 1\n")
    match palabras:
        case "":
            break
        case other:
            lista1.append(palabras)

while True:
    palabras = input("Ingrese palabras a la lista 2\n")
    match palabras:
        case "":
            break
        case another:
            lista2.append(palabras)

print(superposicion(lista1, lista2))