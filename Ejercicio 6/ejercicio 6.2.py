class Nombre:
    name = "Luca"


class Nota:
    grades = 6


class Alumno:
    nombre = Nombre()
    calificacion = Nota()


estudiante = Alumno()
print("Nombre:", estudiante.nombre.name)
print("Nota del examen:", estudiante.calificacion.grades)
if estudiante.calificacion.grades <= 5:
    print("Has desaprobado el examen")
elif estudiante.calificacion.grades >= 6:
    print("Has aprobado el examen")
