# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:26:57 2019

@author: poloXO
"""
# Ejercicio 11: Eficiencia de combustible
# En los Estados Unidos, la eficiencia del combustible para vehículos se expresa normalmente en millas por galón (MPG). 
# En México, la eficiencia del combustible normalmente se expresa en litros por cien kilómetros (L / 100 km). 
# Usa tus habilidades de investigación para determinar cómo convertir de MPG a L / 100 km. 
# Luego crea un programa que lea un valor del usuario en unidades estadounidenses y muestre la eficiencia de combustible equivalente en unidades mexicanas.
# convercion 1 mpg = 235.21 l/100km, la conversion seria es 235.21/ MPG para obtener l/100km
EUA= float(input("La eficiencia en Estados unidos de MPG es:"))
convercion = 235.21 / EUA
print(" La eficiencia de conbustible en Mexico es: %.2f"% convercion, "L/100km")

