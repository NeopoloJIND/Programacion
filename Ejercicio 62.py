## Ejercicio 62
# Un supermercado está ofreciendo el 60% de descuento en una variedad de productos descontinuados. 
# El supermercado quiere ayudar a sus clientes a determinar el precio reducido de su mercancía con una tabla impresa en los aparadores 
# donde muestre los precios originales y los precios después de aplicarse el descuento. 
# Escribe un programa que use un ciclo “while” para generar esa tabla, 
# mostrando el precio original, el descuento y el nuevo precio para los productos de: 
# $4.95
# $9.95
# $14.95
# $19.95
# $24.95
# Los descuentos y los nuevos precios deben ser redondeados a dos decimale
print('precio original   | Descuento | Precio total')
print('--------------------------------------------')
Original = 4.95
while Original <= 24.95:
    Descuento = Original * 0.60
    final = Original - Descuento
    print(' $%.2f''            |' %Original, '$%.2f''     |' %Descuento, '$%.2f' %final )
    Original = Original + 5
