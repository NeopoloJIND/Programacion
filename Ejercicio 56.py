#ejercicio56
#A particular cell phone plan includes 50 minutes of air time and 50 text messages
#for $15.00 a month. Each additional minute of air time costs $0.25, while additional
#text messages cost $0.15 each. All cell phone bills include an additional charge of
#$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
#subject to 5 percent sales tax.
#Write a program that reads the number of minutes and text messages used in a
#month from the user. Display the base charge, additional minutes charge (if any),
#additional text message charge (if any), the 911 fee, tax and total bill amount. Only
#display the additional minute and text message charges if the user incurred costs in
#these categories. Ensure that all of the charges are displayed using 2 decimal places.
txll=.25
txx=.15
ca=.44
j= float()
j2=float()
minutos=int(input('ingrese minutos en un mes: '))
mensajes=int(input('ingrese mensajes en un mes: '))
if minutos == 50:
    print('No se cobra nada por llamdas extras')
elif mensajes == 50:
    print('no se cobra nada por mensajes extras')
elif minutos > 50:
    j=(minutos*txll)
elif mensajes > 50:
    j2=(mensajes*txx)
print('total de cargo extra ', j+j2)
print('total a pagar con timepo extra mas impuestos ', 50+ j + j2 + ca)

