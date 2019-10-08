# ejercicio30
# En este ejercicio creará un programa que lee la presión del usuario en kilopascales. Una vez que se 
#ha leído la presión, su programa debe informar el equivalente
# presión en libras por pulgada cuadrada, milímetros de mercurio y atmósferas. Utilizar
# sus habilidades de investigación para determinar los factores de conversión entre estas unidades.


k=float(input("Ingrese los kilopascales:"))
Mi = k * (760 / 101.325)
Atm = k * (1/ 101.3)
print("en mmHg tu resultado es", Mi)
print("tu resultado en atm es ", Atm)