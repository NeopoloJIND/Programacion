# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:37:09 2019

@author: poloXO
"""

#Ejercicio 7
# escriba  un programa  que lea un numero positivo (n). insertado por el usuario y despues despliegue la suma de todos los enteros
#desde 1 hasta n positivos puede ser  calculado usando usando la formula.


n=int(input("ingresa tu numero:"))
operaciones= n * (n + 1) //2
print("la suma del numero",n,"su calculo es:",operaciones)