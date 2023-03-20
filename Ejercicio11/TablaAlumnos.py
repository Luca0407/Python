import sqlite3


def main():
    print("""Lista de alumnos
Emanuel
Juan
Luca
Juan
Camila
Enzo
Eduardo
Javier
María
Milena
        """)

    nombre = input("Inserte el nombre de un alumno para más info ")
    if alumno(nombre):
        pass


def alumno(nombre):
    conn = sqlite3.connect('estudiantes.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM alumnos WHERE nombre='{nombre}'"
    rows = cursor.execute(query)
    print(rows.fetchmany(2))

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
