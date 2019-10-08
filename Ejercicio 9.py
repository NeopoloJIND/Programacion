# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:50:43 2019

@author: poloXO
"""

506/5000
#Ejercicio 9:
#Interés compuesto.
#Usted  acaba de abrir una nueva cuenta de ahorros que genera un interés del 4%
#por año. El interés que gana se paga al final del año y se agrega
#al saldo de la cuenta de ahorro. Escriba un programa que comience leyendo el
#cantidad de dinero depositada en la cuenta del usuario. Entonces su programa debería
#calcule y muestre el monto en la cuenta de ahorros después de 1, 2 y 3 años. Monitor
#cada cantidad para que se redondee a 2 decimales.
interes=0.4
deposito=float(input("Deposito por año:"))
ano1=deposito*interes
ano1t=ano1+deposito
print("Total del primer año",ano1t)


ano2=ano1t*interes
ano2t=ano1t+ano2
print("Total del segundo año",ano2t)

ano3=ano2t*interes
ano3t=ano2t+ano3e
print("Total del tercer año",ano3t)