# Ejercicio 37 
# Escriba un programa que determine el nombre de una forma a partir de su número de lados. 
# Lea el número de lados del usuario y luego informe el nombre apropiado como parte de un mensaje significativo. 
# Su programa debe admitir formas desde 3 hasta 10 lados. 
# Si se ingresa un numero de lados fuera de este rango, entonces su programa debería mostrar un mensaje 
#de error apropiado.

Lados = int(input("Introduce el numero de lados:"))

if Lados == 3:
	print("\n Es un Triangulo.")
elif Lados == 4:
	print("\n Es un Cuadrado.")
elif Lados == 5:
	print("\n Es un Pentagono.")
elif Lados == 6:
	print("\n Es un Hexagono.")
elif Lados == 7:
	print("\n Es un Heptagono.")
elif Lados == 8:
	print("\n Es un Octagono.")
elif Lados == 9:
	print("\n Es un Nonagono.")
elif Lados == 10:
	print("\n Es un Decagono")
else:
	print("\n El numero de lado esta fuera de rango")