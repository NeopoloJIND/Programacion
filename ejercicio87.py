# EJERCICIO 87

# Centrar una cadena en la terminal.
# Escriba una función que tome una cadena de caracteres como primer parámetro y el ancho de
# el terminal en caracteres como su segundo parámetro. Su función debería devolver un nuevo
# cadena que consta de la cadena original y el número correcto de espacios iniciales
# para que la cadena original aparezca centrada dentro del ancho proporcionado cuando está
# impreso. No agregue ningún carácter al final de la cadena. Incluir un programa principal
# eso demuestra tu función.

ANC = 80

def center(s, ancho):
    if ancho < len(s)
    return(s)

spaces =(ancho - len(s)):
    return s
spaces = (ancho - len(s)) // 2
result = " " * spaces + s
return result

def main():
    print(center("A famous Story", ANC))
    print(center("by:", ANC))
    print(center("Someone Famous", ANC))
    print()
    print("Once upon a time...")

main()