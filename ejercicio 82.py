# Ejercicio 82

# 

# En la ciudad de meico la tarifa de tai uber consiste en un precio base de 44 pesos mas 12 pesos por cada kilometro recorrido
# Escriba una funcion que tome la distancia viajada (km) el cual debe ser el unico argumento y regrese la tarifa total como resultado
# Escriba un programa principal que demuestre la funcion.

def tarifa(distancia):
    Total = 44 + distancia*12.00
    return Total

distancia = float(input('Inserta la distancia marcada en Km: '))

cuota = tarifa(distancia)

print('La cuota toal es: ', cuota, 'pesos')