#ejercicio59
#In a particular jurisdiction, older license plates consist of three uppercase letters
#followed by three numbers. When all of the license plates following that pattern had been used, the format was changed to four numbers followed by three uppercase
#letters.
#Write a program that begins by reading a string of characters from the user. Then
#your program should display a message indicating whether the characters are valid
#for an older style license plate or a newer style license plate. Your program should
#display an appropriate message if the string entered by the user is not valid for either
#style of license plate.
placa= input('ingresa placa')
if len(placa) == 6 and placa[0] >= 'A' and placa[0]<= 'Z' and \
    placa [1] > = 'A' and placa[1] <= 'Z' and \
    placa [2] > = 'A' and placa[2] <= 'Z' and \
    placa [3] > = 'A' and placa[3] <= '9' and \
    placa [4] > = 'A' and placa[4] <= '9' and \
    placa [5] > = 'A' and placa[5] <= '9':
        print('tu placa es vieja y valida')
elif len(placa)==7 and placa [0]>= '0' and placa[0] <= '9' and \
    placa [1] > = 'A' and placa[1] <= '9' and \
    placa [2] > = 'A' and placa[2] <= '9' and \
    placa [3] > = 'A' and placa[3] <= '9' and \
    placa [4] > = 'A' and placa[4] <= 'Z' and \
    placa [5] > = 'A' and placa[5] <= 'Z' and \
    placa [6] > = 'A' and placa[6] <= 'Z':
        print('tu placa es nueva y valida')
else:
    print('introduzca una placa valida')