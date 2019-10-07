# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:57:16 2019

@author: poloXO
"""

#ejercicio 6 
#hacer un programa en el que el usuario introdusca el nombre de la comida que hordeno en un restaurante y su precio 
#y despues su programa debe calcular el subtoral,el IVA y la propina  de toda la cuenta. La salida del 
#programa debe parecerse a un ticket de restaurante ..
#iva de 16%
#y una propina del 15% del subtotal 
#Los valores numericos deben tener 2 decimales.

IVA=0.16
Propina=0.15

comida1=(input("Introduzca su comida:"))
precio1=float(input("Introduzca el precio de la comida:$"))
comida2=(input("Introduzca su comida:"))
precio2=float(input("Introduzca el precio de la comida:$"))
comida3=(input("Introduzca su comida:"))
precio3=float(input("Introduzca el precio de la comida:$"))
comida4=(input("Introduzca su comida:"))
precio4=float(input("Introduzca el precio de la comida:$"))
comida5=(input("Introduzca su comida:"))
precio5=float(input("Introduzca el precio de la comida:$"))
print (comida1," $",precio1)
print (comida2," $",precio2)
print (comida3," $",precio3)
print (comida4," $",precio4)
print (comida5," $",precio5)
Subtotal=precio1+precio2+precio3+precio4+precio5
print ("Subtotal:$%.2f" %Subtotal)
Subtotal1=(Subtotal*IVA)
print ("IVA:$%.2f" %Subtotal1)
Subtotal2=(Subtotal*Propina)
print ("Propina:$%.2f" %Subtotal2)
Total=Subtotal+Subtotal1+Subtotal2
print ("Total:$%.2f" %Total)