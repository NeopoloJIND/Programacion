# ejercicio27
#Escribe un programa que calcule el índice de masa corporal (IMC) de un individuo. Tu
#program debería comenzar leyendo una altura y un peso del usuario. Entonces debería
#utilice una de las siguientes dos fórmulas para calcular el IMC antes de mostrarlo. Si
# lees la altura en pulgadas y el peso en libras, entonces el índice de masa corporal es
#computado con la siguiente fórmula:
# IMC = (peso / (altura × altura)) × 703.
# Si lee la altura en metros y el peso en kilogramos, entonces el índice de masa corporal
# se calcula utilizando esta fórmula un poco más simple:
# IMC = peso / altura × altura

A= float(input("Ingrese la altura en metros: "))
P= float(input("Ingrrese el peso en kg: "))
imc= P/(A * A)
print("Su IMC es %.4f" % imc)
