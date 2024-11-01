edad= int(input("Escriba su edad: "))

if edad<=10:
    print ("El monto a cancelar es 3000 colones")
elif edad<=15 and edad>10:
    print("El monto a cancelar es 5000 colones")
elif edad<=18 and edad>15:
    print("El monto a cancelar es 7500 colones")
else:
    print("El monto a cancelar es 10000 colones")