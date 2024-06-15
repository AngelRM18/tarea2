numero=int(input("ingrese un numero:  "))

if numero < 10000:
    print("----sin comision----")
else:
    porcentaje=numero*0.05
    print("----DEBE PAGAR 5%----""A PAGAR:",porcentaje )
    
print("gracias por usar el servicio")      