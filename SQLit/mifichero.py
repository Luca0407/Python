# sistema para verificar contraseña y usuario. Crear usuario
import getpass
import sqlite3

def main():
    crear_usuario(3, "pepe", "superclave")

def main2():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")  # recordemos que para las contraseñas es preferible usar getpass

    if verificar(username, password):
        print("Inicio de sesión correcto")
    else:
        print("Inicio de sesión incorrecto")


def verificar(username, password):
    conn = sqlite3.connect('miaplicacion.db')  # se conecta a la ddbb miaplicacion.db
    cursor = conn.cursor()  # genera un cursor

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"  # fString que toma las
    # variables locales username y password. Toma la id de todos los datos
    rows = cursor.execute(query)  # en user y devolverá la id de aquella con la que ambos datos concuerden.
    rows.fetchone()  # fetchone solamente devuelve 1 elemento de todos los posibles.

    cursor.close()  # cierra un cursor
    conn.close()  # cierra la conexión con la ddbb


def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = '''INSERT INTO users(id, username, password) VALUES(?, ?, ?)'''
    # por lo general no solemos poner los datos directamente en nuestro query, sino que usamos esos signos, los cuales
    cursor.execute(query, (identificador, usuario, clave))  # luego son reemplazados en el execute, añadiendo como
    conn.commit()  # segundo parámetro una tupla con los datos en su orden respectivo. Con commit le enviamos los
    cursor.close()                                                                        # cambios a la base de datos
    conn.close()


if __name__ == '__main__':  # si el nombre del modulo ejecutandose es __main__, que ejecute la función main()
    main()
