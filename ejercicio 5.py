# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:30:21 2019

@author: poloXO
"""
#Ejercicio 5: depósitos de botellas
#(Resuelto — 15 líneas)
#En muchas jurisdicciones se agrega un pequeño depósito a los envases de bebidas para alentar a las personas
#para reciclarlos En una jurisdicción particular, beba recipientes de un litro o
#menos tienen un depósito de $ 0.10, y los recipientes de bebidas que contienen más de un litro tienen
#Depósito de $ 0.25.
#Escriba un programa que lea el número de contenedores de cada tamaño del usuario.
#Su programa debe continuar calculando y mostrando el reembolso que será
#recibido por devolver esos contenedores. Formatee la salida para que incluya un dólar
#firmar y siempre muestra exactamente dos decimales.

Bmenos=.10
Bmas=.25
print ( "Bienvenidos a botellas y dinero..." )
print ("Indique que tamaño es su botella por favor.")
menos=int(input("cuantas botellas chicas ingresate:"))
mas = int(input("cuantas botellas grandes ingresastes:"))
OP=menos*Bmenos+ mas * Bmas
print ("EL total es $ %.2f.", OP)
