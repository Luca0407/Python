year = input("inserte el año: ")


def esbisiesto():
    if int(year) % 4 == 0:
        return year + " es bisiesto"
    else:
        return "no es bisiesto"


sera = esbisiesto()
print(sera)
