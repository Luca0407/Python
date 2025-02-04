"""
5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una
lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
lista = [1, 2, 3, 4, 5]


def summ(lis):
    total = 0
    for i in lis:
        total += i

    print(f"{total}\n")


def multip(lis):
    total = 1
    for i in lis:
        total *= i

    print(f"{total}\n")


while True:
    val = input("¿suma o multiplicacion?\n(escriba 'salir' para cerrar.)\n")
    match val.lower():
        case "suma":
            summ(lista)
        case "multiplicacion":
            multip(lista)
        case "salir":
            break
        case other:
            print("Valor no valido.\n")
