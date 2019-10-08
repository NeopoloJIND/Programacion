# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:51:01 2019

@author: poloXO
"""
#Ejercicio 17: capacidad calorífica
#(Resuelto — 25 líneas)
#La cantidad de energía requerida para aumentar la temperatura de un gramo de material.
#en un grado Celsius es la capacidad de calor específica del material, C. La cantidad total
#de energía requerida para elevar m gramos de un material en ΔT grados Celsius puede ser
#calculado usando la fórmula:
#q = mCΔT.
#Escriba un programa que lea la masa de un poco de agua y el cambio de temperatura.
#del usuario Su programa debe mostrar la cantidad total de energía que debe ser
#agregado o eliminado para lograr el cambio de temperatura deseado.
#Sugerencia: La capacidad calorífica específica del agua es 4.186 J
#g◦C. Porque el agua tiene una densidad
#de 1.0 gramo por mililitro, puede usar gramos y mililitros indistintamente
#en este ejercicio
#Extienda su programa para que también calcule el costo de calentar el agua. Electricidad
#normalmente se factura utilizando unidades de kilovatios hora en lugar de julios. En este
#ejercicio, debe suponer que la electricidad cuesta 8,9 centavos por kilovatio-hora. Utilizar
#su programa para calcular el costo de hervir agua por una taza de café.


agua=4.186
ele= 8.9
J= 2.7777e-7

Volumen =float(input("inserte los mililitros de agua:"))
Dtemperatura=float(input( "inserte la temperatura en grados celcius:"))
q= Volumen * Dtemperatura * agua
print (" usted requiere %d joules de energia" % q )
kilovatios= q*J
costo =kilovatios * ele
print ( "la energia del costo  es en  centavos  : ", costo)



