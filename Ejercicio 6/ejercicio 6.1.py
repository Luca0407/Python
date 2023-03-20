class Vehiculo:
    color = "rojo"
    ruedas = 4
    puertas = 5


class Coche(Vehiculo):
    velocidad = 0  # actual
    cilindrada = 6


auto = Coche()
print("el auto es de color ", auto.color)
print("el auto tiene", auto.ruedas, "ruedas")
print("el auto tiene", auto.puertas, "puertas")
print("su velocidad máxima es de", auto.velocidad + 180, "KM/H")
print("el auto tiene", auto.cilindrada, "cilindros")
