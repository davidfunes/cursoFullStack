# Es año bisiesto

# p : es divisible entre 4
# q : es divisible entre 100 (¬q no es divisible entre 100)
# r : es divisible entre 400

# p ^ (¬q V r)

def esBisiesto (ano):
    if ano < 1582:
        return False
    elif ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
        return True
    else:
        return False

ano = int(input('Introduce un año para saber si es bisiesto: '))

if esBisiesto(ano):
    print("El año", ano, "es bisiesto!")
else:
    print("El año", ano, "no es bisiesto.")




