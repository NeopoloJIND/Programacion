## Ejercicio 78
# Escriba un programa que convierta un numero decimal (base 10) que inserte un usuario como numero entero
# y después use el algoritmo de división mostrado para realizar la conversión. 
#Cuando el algoritmo se complete el resultado deberá contener la representación del numero en binario. 
# Después se deberá desplegar el resultado con el mensaje apropiado.
# Sea resultado una variable string vacía.
# Sea “q” un numero entero a convertir
# Repetir:
   # Sea “r” igual al residuo cuando “q” es dividido entre 2.
   # Convertir “r” a string y agregándolo al comienzo de resultado
   # Dividir “q” entre 2 , eliminar cualquier residuo y guardar el resultado de nuevo en “q”
# Hasta que “q” sea cero

resultado = ""
Q = int(input("Inserta el numero:"))

r = Q % 2
resultado = str(r) + resultado

Q = Q // 2
while Q> 0:
    r = Q % 2
    resultado = str(r) + resultado
    Q = Q // 2 

print('binaro', resultado)

