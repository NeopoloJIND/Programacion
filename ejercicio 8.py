# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:43:52 2019

@author: poloXO
"""
#Cajas de cereal.
#Un vendedor de una pagina de abarrotes en linea vende dos tipos de cajas de cereal,cornflakes
#de 750gr y Trix de 500gr.Escriba un programa que lea el numero  de cajas de cornFlakes y cajas 
#de trix , cuyo valor debe de ser introduccido por el usuario .Despues su programa debe calcular
#y mostrar el peso en kilogramos del envio. 
Corn=int(input("cajas por ordenar:"))
Trix=int(input("cajas por ordenar:"))
peso1=float(Corn*.75)
peso2=float(Trix*.5)
suma=peso1+peso2

print ("El peso total es:", suma,"Kg")

