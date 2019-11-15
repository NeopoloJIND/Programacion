# Ejercicio 35
# Se dice comúnmente que un año humano es equivalente a 7 años de perro. 
# Sin embargo, esta simple conversión no reconoce que los perros alcanzan la edad adulta en aproximadamente dos años. 
# Como resultado, algunas personas creen que es mejor contar cada uno de los primeros dos años humanos como 10.5 años de perro, 
# y luego contar cada año humano adicional como 4 años de perro.
# Escriba un programa que implemente la conversión de años humanos a años de perros descritos en el párrafo anterior. 
# Asegúrese de que su programa funcione correctamente para conversiones de menos de dos años humanos y para 
#conversiones de dos o más años humanos. Su programa debe mostrar un mensaje de error apropiado si el usuario ingresa un número negativo.

Humano = int(input("Ingrese la edad de un perro en años humanos: "))


	
if Humano > 0:
	perro = Humano * 10.5
elif Humano <= 2:
	
	perro = 21 + (Humano-2) * 4

if Humano == 0:
	print("Por favor ingrese un entero positivo.")
else:
	print("El perro tiene",(perro), "años.")