"""
3- Definir una función que calcule la longitud de una lista o una cadena dada (es cierto que python tiene la función
len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio).
"""
lista = []
palabra = "adadasdafdfsg"
contador = 0


def largoLista(l, c, pal):
    while pal != "":
        pal = input("ingrese una palabra")
        if pal != "":
            l.append(pal)
    for i in l:
        c += 1

    print(f"la lista tiene una longitud de {c}")


def largoCadena(p, c):
    p = input("¿Cuál es la palabra?")
    for i in p:
        c += 1

    print(f"la cadena tiene una longitud de {c}")


while True:
    opcion = int(input("¿De qué quiere calcular su longitud?\n[1] lista\n[2] cadena\n"))
    match opcion:
        case 1:
            largoLista(lista, contador, palabra)
            break
        case 2:
            largoCadena(palabra, contador)
            break
        case other:
            print("dato inválido")

