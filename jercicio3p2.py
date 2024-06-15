n1 = int(input("Ingrese la nota 1: "))
n2 = int(input("Ingrese la nota 2: "))
n3 = int(input("Ingrese la nota 3: "))
n4 = int(input("Ingrese la nota 4: "))

promedio = (n1 + n2 + n3 + n4) / 4

if 1 <= promedio <= 10:
    letra = 'F'
elif 11 <= promedio <= 20:
    letra = 'E'
elif 21 <= promedio <= 30:
    letra = 'D'
elif 31 <= promedio <= 40:
    letra = 'C'
elif 41 <= promedio <= 50:
    letra = 'B'
elif 51 <= promedio <= 100:
    letra = 'A'
else:
    letra = 'Promedio fuera de rango'

print("El promedio de las notas es: ", promedio)
print("La letra correspondiente al promedio es: ",letra)
print("Gracias por usar el servicio")     