from functools import reduce


lista = []
for numeros in range(1, 100):
    lista.append(numeros)

filtro = filter(lambda x: x % 2 != 0, lista)


def suma(a, b):
    return a + b


resultado = reduce(suma, list(filtro))
print(resultado)
