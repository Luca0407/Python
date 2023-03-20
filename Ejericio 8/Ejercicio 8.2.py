import pickle


class Vehiculo:
    ruedas = 0
    puertas = 0
    motor = None

    def __init__(self, ruedas, puertas, motor):
        self.ruedas = ruedas
        self.puertas = puertas
        self.motor = motor

    def __str__(self):
        return f'Este vehiculo tiene {self.ruedas} ruedas, {self.puertas} puertas y un motor eléctrico ({self.motor})'


auto = Vehiculo(4, 3, True)

f2 = open("vehiculo.bin", 'wb')
pickle.dump(auto, f2)
f2.close()

f2 = open("vehiculo.bin", 'rb')
carro = pickle.load(f2)
f2.close()
print(carro.__str__())
