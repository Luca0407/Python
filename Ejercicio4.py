"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

letra = "f"
while True:
    letra = input("ingrese una letra\n")
    if len(letra) > 1 or len(letra) == 0:
        print("letra invalida.\n")
        continue

    match letra.lower():
        case "a":
            print(True)
        case "e":
            print(True)
        case "i":
            print(True)
        case "o":
            print(True)
        case "u":
            print(True)
        case other:
            print(False)
