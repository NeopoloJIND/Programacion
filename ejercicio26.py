#ejercicio26
#(En este ejercicio usted revertira el proceso descrito en el ejercicio previo. Desarrole un programa que comienze por leer una cantidad de segundos introducidos por el usuario. Su programa debe desplegar la cantidad equivalente en la forma de D:HH:SS, donde D son los dias, HH son las horas, MM son los minutos y SS son los segundos. Las horas, minutos y segundos deben estar en formato de 2 digitos con un 0 al inicio, si es necesario.)
segundos=int(input("Inserte segundos:"))
Segundos_por_hora=86400
segundos_por_hora=3600
segundo_por_minuto=60

dia= segundos / Segundos_por_hora
segundo = segundos % Segundos_por_hora

hora= segundos / segundos_por_hora
segundo = segundos % segundos_por_hora

minutos= segundos / segundo_por_minuto
segundo= segundos % segundo_por_minuto

print("tiempo =", "%2.2f" % dia, "%2.2f" % hora, "%2.2f" % minutos, "%2.2f" % segundo)


