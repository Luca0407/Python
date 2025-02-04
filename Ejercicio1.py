"""
1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos (es cierto que python
tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""


def maxx(x, y):
    if x > y:
        print(f"el número mayor es {x}")
    else:
        print(f"el número mayor es {y}")


num1 = int(input("Ingrese un número\n"))
num2 = int(input("Ingrese otro número\n"))

maxx(num1, num2)
