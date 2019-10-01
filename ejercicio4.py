# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:55:43 2019

@author: poloXO
"""

#Crear unprograma que lea el largo y ancho de un cammpo de cultivo
#introducciendo el usuario y despliegue el area del campo de acres.

Largo = float ( input ("inserte el  largo en metros:"))
Ancho = float ( input ("inserte  el ancho en metros:"))
print ("El area del campo  es", Largo*Ancho*.000247105 , "en acres")


