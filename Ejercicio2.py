"""
2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""


def maxx(x, y, z):
    if x > y and x > z:
        print(f"el número mayor es {x}")
    elif y > z and y > x:
        print(f"el número mayor es {y}")
    else:
        print(f"el número mayor es {z}")


num1 = int(input("Ingrese un número\n"))
num2 = int(input("Ingrese otro número\n"))
num3 = int(input("Ingrese otro número más\n"))

maxx(num1, num2, num3)
