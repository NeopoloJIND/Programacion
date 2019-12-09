# EJERCICIO 85

# Mediana de tres valores.
# Escriba una función que tome tres números como parámetros y devuelva el valor medio
# de esos parámetros como resultado. Incluya un programa principal que lea tres valores de
# el usuario y muestra su mediana.

# Sugerencia: el valor medio es el medio de los tres valores cuando se ordenan
# en orden ascendente. Se puede encontrar usando declaraciones if, o con un poco de
# creatividad matemática.

def mediana(a, b, c):
    ifv  a < b and b < c or a > b and b > c:
        return b
    if b < a and a < c or b > a and a > c:
        return
    if c < a and b < c or c > a and b > c:
        return c

def alternarmediana(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

def main():
    x = float(input('Introduce el primer valor: '))
    y = float(input('Introduce el segundo valor: '))
    z = float(input('Introduce el tercer valor: '))

    print('El valor medio es ', mediana(x, y, z))
    print('Usando el metodo alternativo, esto es: ', alternarmediana(x, y, z))
main()