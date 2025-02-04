"""
6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería
devolver la cadena "odnaborp yotse"
"""
def inversa(cadena):
    pal = ""
    for i in reversed(cadena):
        pal += i

    print(pal)


palabra = input("¿Qué palabra quiere invertir?\n")

inversa(palabra)
