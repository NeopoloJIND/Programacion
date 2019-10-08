# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:36:03 2019

@author: poloXO
"""
#Ejercicio 12.
#Distancia entre dos puntos de la tierra.
#La superficie de la tierra es curva y la distancia entre grados  de longitud varia con la longitud,como resultado,
#encontrar la distancia entre dos puntos  de la superfie de la tierra es mas complicado que usar el teorema de pitagoras.
#Si(t1,g1) y (t2,g2) es la latitud y longitud de dos puntos de la superfice de la tierra,, en kilometros es:
import math
lat1=float(input("ingresa la latitud a:"))
lon1=float(input("ingresa la longitud a:"))
lat2=float(input("ingresa la latitud b:"))
lon2=float(input("ingresa la longitud b:"))
t1=math.radians (lat1)
t2=math.radians (lat2)
g1=math.radians (lon1)
g2=math.radians (lon2)

distancia= 6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))

print("La distancia entre los puntos es:", distancia,"km")

