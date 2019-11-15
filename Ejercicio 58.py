#ejercicio 58
#Write a program that reads a date from the user and computes its immediate successor.
#For example, if the user enters values that represent 2013-11-18 then your program
#should display a message indicating that the day immediately after 2013-11-18 is
#2013-11-19. If the user enters values that represent 2013-11-30 then the program
#should indicate that the next day is 2013-12-01. If the user enters values that represent
#2013-12-31 then the program should indicate that the next day is 2014-01-01. The
#date will be entered in numeric form with three separate input statements; one for
#the year, one for the month, and one for the day. Ensure that your program works
#correctly for leap years.

an= int(input("ingrese anio"))
	
if (an % 400 == 0):
    anio_bisiesto = True
elif (an % 100 == 0):
    anio_bisiesto = False
elif (an % 4 == 0):
    anio_bisiesto = True
else:
    anio_bisiesto = False
    
mes = int(input("ingrese mes [1-12]: "))

if mes in (1, 3, 5, 7, 8, 10, 12):
    tammes = 31
elif mes == 2:
    
    if anio_bisiesto:
        tammes = 29
   
    else:
        tammes = 28
    
else:
    tammes = 30
	
dia = int(input("ingrese dia [1-31]: "))
	
if dia < tammes:
    dia += 1
else:
    dia = 1
    if mes == 12:
        mes = 1
        an += 1
	
    else:
        mes += 1
print("el siguiente dato es [yyyy-mm-dd] %d-%d-%d." % (an, mes, dia))