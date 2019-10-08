# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 00:20:34 2019

@author: poloXO
"""
#Ejercicio 19: 
#Caída libre
#Cree un programa que determine qué tan rápido viaja un objeto cuando golpea el
#suelo. El usuario ingresará la altura desde la cual se cae el objeto en metros (m).
#Debido a que el objeto se cae, su velocidad inicial es de 0 m / s. Supongamos que la aceleración
#debido a la gravedad es de 9.8m / s2. Puedes usar la fórmula vf =sqrt(vi^2o + 2ad ) y para calcular el
#velocidad final, vf, cuando se conoce la velocidad inicial, vi, aceleración, a y distancia, d.
import math


V0=float(input("Ingresa la velocidad inicial:"))
G=float(input("Ingresa la gravedad:"))
d=float(input("Ingresa la distancia:"))


VF=math.sqrt(V0*V0)+math.sqrt(2*G*d)

print("La velocidad final es:", VF,"m/s")