# EJERCICIO 89
# Capitalizarlo:
# Muchas personas no usan letras mayúsculas correctamente, especialmente cuando escriben en letra pequeña
# dispositivos como teléfonos inteligentes. En este ejercicio, escribirás una función que capitaliza
# Los caracteres apropiados en una cadena. Una "i" minúscula debe ser reemplazada por una
# "I" mayúscula si está precedido y seguido por un espacio. El primer personaje en
# la cadena también debe estar en mayúscula, así como el primer carácter no espacial después de un
# ".", "!" O "?". Por ejemplo, si la función se proporciona con la cadena "a qué hora
# ¿Tengo que estar allí? ¿cuál es la dirección? ", entonces debería devolver la cadena" What
# tiempo tengo que estar allí? ¿Cual es la dirección?". Incluya un programa principal que lea
# una cadena del usuario, la capitaliza utilizando su función y muestra el resultado.


def capitalize(s):
    result = s.replace("i","I")
    
    if len(s) > 0:
        result = result[0].upper() + \
            result[1 : len(result)]
    
    Pos = 0
    while Pos < len(s):
        if result[Pos] == "." or result[Pos] == "!" or result [Pos]=="?":
            Pos =Pos + 1
            
            while Pos < len(s) and result[Pos] == " ":
                Pos = Pos + 1
            
            if Pos < len(s):
                result = result[0 : Pos] + \
                    result[Pos].upper() + \
                    result[Pos + 1 : len(result)]
    Pos = Pos+1
    return result
def main():
    s = input("introduzca texto: ")
    capitalized = capitalize(s)
    print("la capitalicacion es:  ", capitalized)
main()