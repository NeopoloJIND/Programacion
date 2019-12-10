# EJERCICIO 91

# Precedencia del operador:
# Escriba una función llamada precedencia que devuelva un número entero que represente la precedencia
# de un operador matemático. Una cadena que contiene el operador se pasará a
# la función como su único parámetro. Su función debe devolver 1 para + y -, 2 para *
# y /, y 3 para ˆ. Si la cadena pasada a la función no es uno de estos operadores
# entonces la función debería devolver -1. Incluya un programa principal que lea un operador
# del usuario y muestra la precedencia del operador o un mensaje de error que indica
# que la entrada no era un operador. Su programa principal solo debe ejecutarse cuando
# el archivo que contiene su solución no se ha importado a otro programa.

def precedence(operacion):
    operacion = operacion.strip()
    if (operacion == '+') or (operacion == '-'): 
        return 1
    elif (operacion == '*') or (operacion == '/'): 
        return 2
    elif (operacion == '^'):
        return 3
    else: 
        return -1
    
    
def main():    
    op = input("Ingrese el símbolo de la operación que desea evaluar: ")

    resultado = precedence(op)
    if resultado == -1: 
        print("El símbolo ingresado no es una operación válida")
    else: 
        print(resultado)
main()