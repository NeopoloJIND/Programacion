# -*- coding: utf-8 -*-
"""
Created on Tus Oct  5 11:20:50 2019

@author: poloXO
"""
#Ejercicio 16: 
#área y volumen
#Escriba un programa que comience leyendo un radio, r, del usuario. El programa
#continúe calculando y mostrando el área de un círculo con radio r y el
#volumen de una esfera con radio r. Use la constante pi en el módulo matemático en su
#cálculos
#Sugerencia: El área de un círculo se calcula utilizando el área de fórmula = πr 2. El
#El volumen de una esfera se calcula utilizando la fórmula volumen = 4
#3πr^3.
import math
pi=3.1416
r=float(input("Inserte el radio:"))
area=float((pi)*(r*r))
volumen=float((3/4)*(pi)*(r*r*r))
print("Area del circulo:",area)
print("Volumen de la esfera:", volumen)