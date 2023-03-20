# codigo solamente funcional en python. Forma de obtener e imprimir los usuarios
# y directorios del dispositivo (desde el fichero usado). Luego filtramos con
# split para solo queden los nombres de usuario, y con una lista vacia los
# imprimimos para que se vea mejor.

def main():
    usuarios = listarusuarios()
    for usuario in usuarios:
        print(f'usuario: {usuario}')


def listarusuarios():
    fichero = open('/etc/passwd', 'r')
    datos = fichero.readlines()
    fichero.close()

    resultado = []

    for linea in datos:
        if linea[0] == '#' or linea[0] == '_':
            continue

        partes = linea.split(':')
        resultado.append(partes[0])
        return resultado


if __name__ == '__main__':
    main()
