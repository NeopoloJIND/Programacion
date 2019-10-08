# ejercicio28
# Cuando el viento sopla en clima frío, el aire se siente aún más frío de lo que realmente es
# porque el movimiento del aire aumenta la velocidad de enfriamiento de los objetos calientes, como
# personas. Este efecto se conoce como sensación térmica.
# En 2001, Canadá, el Reino Unido y los Estados Unidos adoptaron la siguiente fórmula para calcular 
#el índice de sensación térmica. Dentro de la fórmula Ta está el
# la temperatura del aire en grados Celsius y V es la velocidad del viento en kilómetros por hora.
# Se puede usar una fórmula similar con diferentes valores constantes con temperaturas en
# grados Fahrenheit y velocidades del viento en millas por hora.
# WCI = 13.12 + 0.6215Ta - 11.37V 0.16 + 0.3965TaV 0.16
# Escriba un programa que comience leyendo la temperatura del aire y la velocidad del viento del
#usuario. Una vez que se hayan leído estos valores, su programa debería mostrar la sensación térmica
#index redondeado al entero más cercano.
import math
T= float(input("Ingrese temperatura en grados F;"))
V= float(input("Ingrese velocidad en km: "))
WCI= 13.12 + (0.6215 * (T)) - (11.37 * (math.pow(V, 0.16))) + (0.3965* (T)* (math.pow(V, 0.16))) 
print("La sensacion termica es %.4f" % WCI)