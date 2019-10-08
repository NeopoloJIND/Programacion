#Ejercicio25
#(Crear un programa que le pida al usuario la duracion en dias, horas, minutos y segundos. 
#Calcular y desplegar la cantidad totalde segundos de duracion.)
Di= float(input("Inserte los dias:"))
Ho= float(input("Inserte las horas: "))
Mi= float(input("Inserte los minutos:"))
Se= float(input("inserte los segundos:"))

Dias = Di*86400
Horas =Ho*3600
Minutos=Mi*60
Segundos=Se*1

Totaldesegundos = Dias+Horas+Minutos+Segundos
print("La cantidad en segundos son:",Totaldesegundos)
