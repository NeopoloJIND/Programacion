# ejercicio29
#Escribe un programa que comienza leyendo una temperatura del usuario en grados
#Celsius. Entonces su programa debe mostrar la temperatura equivalente en grados
#Fahrenheit y grados Kelvin. Los cálculos necesarios para convertir entre diferentes
#unidades de temperatura se pueden encontrar en internet.

Cel=float(input("Ingrese temperatura en grados celcius:"))
F=(9/5 * Cel) + 32
print("Fahrenheit %.4f" % F)