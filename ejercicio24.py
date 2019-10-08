#Ejercicio 24:
#Unidades de tiempo
#Cree un programa que lea una duración del usuario como un número de días, horas,
#minutos y segundos. Calcule y muestre el número total de segundos representados
#por esta duración.

h= int(input("Ingrese horas"))
m= int(input("Ingrese minutos"))
s= int(input("Ingrese segundos"))
HO= h * 3600
MI= m * 60
Ts= HO + MI + s
print('los segundos totateles son ', Ts)