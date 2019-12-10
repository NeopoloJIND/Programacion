# EJERCICIO 93

# Próximo siguiente
# En este ejercicio creará una función llamada nextPrime que encuentra y devuelve
# el primer número primo más grande que un número entero, n. El valor de n se pasará a
# la función como su único parámetro. Incluya un programa principal que lea un número entero de
# el usuario y muestra el primer número primo mayor que el valor ingresado. Importar
# y use su solución para el Ejercicio 92 mientras completa este ejercicio.

def nextPrime(num):
    while True: 
        if num < 0: 
            print("www")
            print("El número no es un entero positivo")
            num = float(input("Ingrese un número entero positivo: "))
        elif num != int(num): 
            print("El número no es un entero positivo")
            num = float(input("Ingrese un número entero positivo: "))
        else: 
            break
    num = int(num)
    num = num+1
    while True:
        for i in range(2,num): 
            if num%i == 0: 
                num = num+1
                break
        else: 
            print("El primero primo más grande que el número ingresado es: ", n)
            break

def main():
    number = float(input("Ingrese un número entero positivo: "))
    nextPrime(number)

main()
