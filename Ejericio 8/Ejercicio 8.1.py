f = open('mensajes.txt', 'w')
saludo = f.write("Hola!\n")
presentacion = f.write("soy un archivo de texto.")
f.close()

f = open('mensajes.txt', 'r')
leer = f.read()
f.close()
print(leer)
