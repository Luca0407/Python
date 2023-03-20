import time


hora = time.strftime('%H')
minutos = time.strftime('%M')
print("Son las", hora + ":" + minutos)


if int(hora) >= 19:
    print("Ya podes irte a casa!")
elif int(minutos) == 0:
    print("Faltan {} hora(s) para terminar por hoy".format(18 - int(hora)))
elif int(hora) == 18:
    print("Faltan {} minuto(s) para terminar por hoy".format(59 - int(minutos)))
else:
    print("Faltan {} hora(s) y {} minuto(s) para terminar por hoy".format(18 - int(hora), 59-int(minutos)))
