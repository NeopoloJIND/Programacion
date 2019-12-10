# EJERCICIO 99

# Conversiones de bases arbitrarias:
# Escriba un programa que permita al usuario convertir un número de una base a otra.
# Su programa debe admitir bases entre 2 y 16 para el número de entrada y
# El número de resultado. Si el usuario elige una base fuera de este rango, entonces un apropiado
# Se debe mostrar un mensaje de error y el programa debe salir. Divide tu programa
# en varias funciones, incluida una función que convierte de una base arbitraria a
# base 10, una función que convierte de base 10 a una base arbitraria, y una
# programa que lee las bases y el número de entrada del usuario. Puedes encontrar tu
# Las soluciones a los ejercicios 77, 78 y 98 son útiles al completar este ejercicio.
from hex_digit import*
 
def dec2n(num, new_base):
     result=""
     q= num
     r= q % new_base
     result= int2hex(r) + result
     q= q//new_base
     
     while q > 0:
         r= q % new_base
         result = int2hex(x) + result
         q = q // new_base
     return result
def n2dec(num, b):
    decimal=0
    power=0
    
    for i in range (len(num)):
        decimal = decimal * b
        decimal = decimal + hex2int(num[i])
    return decimal
def main():
    from_base=int(input("enter the base to convert from: "))
    from_num =input("Enter a sequence of digits in that base: ")
    
    dec = n2dec(from_num, from_base)
    print("that's %d in base10." % dec)
    
    
    to_base= int(input("enter the base to convert to :"))
    to_num = dec2n(dec, to_base)
    print ("that's %s in base %d." % (to_num, to_base))
    
 