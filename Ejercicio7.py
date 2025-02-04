"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto
escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""
def inversa(word):
    pal = ""
    for i in reversed(word):
        pal += i

    return pal


def es_palindromo(cadena):
    if cadena == inversa(cadena):
        return True
    else:
        return False


palabra = input("Introduzca una palabra para saber si es un palíndromo\n")

print(es_palindromo(palabra))
