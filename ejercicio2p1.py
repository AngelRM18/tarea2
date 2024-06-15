color1 = input("Ingrese el primer color (azul, verde, rojo): ")
color2 = input("Ingrese el segundo color (azul, verde, rojo): ")

def mezclar_colores(color1, color2):
    if (color1 == 'azul' and color2 == 'verde') or (color1 == 'verde' and color2 == 'azul'):
        return 'cian'
    elif (color1 == 'verde' and color2 == 'rojo') or (color1 == 'rojo' and color2 == 'verde'):
        return 'marrón'
    elif (color1 == 'azul' and color2 == 'rojo') or (color1 == 'rojo' and color2 == 'azul'):
        return 'morado'
   
resultado = mezclar_colores(color1, color2)

print("La mezcla de los colores es:", resultado)
print("Gracias por usar el servicio")