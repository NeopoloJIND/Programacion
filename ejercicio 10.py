# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:07:43 2019

@author: poloXO
"""
#cree un programa que lea dos valores enteros, a y b , introducciodos por el usuario . su
#programa debe desplegar:
#-La suma de (a y b)
#-La diferencia cuando a es sustraidos a b.
#-El producto de( a( y( b).
#-El cociente cuando a divide a b.
#-El residuo cuando a divide a b.
#-El resultado de log (a)
#-El resultado de a a la potencia b.
#Tip: utilice la libreria math.
from math import log
a = int(input("insete el valor de a: "))
b = int(input("insete el valor de b: "))
print("")
print(a, "+", b, "es: ", a+b)
print("")
print(a, "-", b, "es: ", a-b)
print("")
print (a, "*", b, "es:", a*b)
print("")
print(a, "/", b, "es:", a/b)
print("")
print(a, "%", b, "es:", a%b)
print("")
print("El logaritmo para", a, "es: %.2f" % log(a))
print("")
print(a, "^", b, "es: ", a**b)
