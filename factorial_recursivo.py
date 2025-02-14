"""
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.
"""
def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x-1)

num = int(input("Ingrese un número para calcular su factorial\n> "))

print(f"El factorial de {num} es: {fact(num)}")