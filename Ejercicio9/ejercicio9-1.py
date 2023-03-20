items = input("Escribe países separados por comas:\n")

paises = [pais for pais in items.split(",")]

print(",".join(list(set(sorted(paises)))))
