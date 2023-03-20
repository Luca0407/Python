import operaciones.resta.Resta as Res
import operaciones.suma.Suma as Sum
import operaciones.divi.Division as Div
import operaciones.multi.Multiplicacion as Mul


def calculo():
    print(Res.restar(3, 3))
    print(Sum.sumar(3, 3))
    print(Div.dividir(3, 3))
    print(Mul.multiplicar(3, 3))


calculo()
