#Ejercicio 33: Pan de un día
#Una panadería vende hogazas de pan por $ 3.49 cada una. El pan de un día tiene un descuento de 60
#por ciento. Escriba un programa que comience leyendo la cantidad de panes de un día
#pan que se compra al usuario. Entonces su programa debe mostrar el regular
#precio del pan, el descuento porque tiene un día y el precio total. Toda la
#los valores deben mostrarse con dos decimales y los puntos decimales en todos
#de los números deben alinearse cuando el usuario ingresa valores razonables.
#Las construcciones de programación que usaste para resolver los ejercicios en el anterior
#El capítulo seguirá siendo útil a medida que aborde estos problemas. además, el
#Los ejercicios de este capítulo requerirán que utilice construcciones de toma de decisiones para que
#sus programas pueden manejar una variedad de situaciones diferentes que puedan surgir.
#espere usar algunas o todas estas características de Python al completar estos problemas:
#• Tomar una decisión con una declaración if
#• Seleccione una de dos alternativas con una declaración if-else
#• Seleccione una de varias alternativas utilizando una instrucción if-elif o if-elif-else
#• Construya una condición compleja para una instrucción if que incluya los operadores booleanos
#y, o y no
#• Anide una declaración if dentro del cuerpo de otra declaración if
Pan=int(input("ingrese cantidad de panes:"))
Des=.60
Prec=3.49
operacion1=(Pan*Prec)
operacion2=operacion1*.60
operacion3=(operacion1-operacion2)
print("precio del pan sin descuento " "%.2f" % operacion1, "|", "decuento " "%.2f" % operacion2, "|", "precio total con descuneto " "%.2f" % operacion3)