numero = int(input("Ingrese el numero : "))
if (numero%3)==0 and (numero%5)==0:
    print("Es numero magico")
elif (3%numero)==0:
    print("Divisible por 3")
elif(5%numero)==0:
    print("Divisible por 5")
else:
    print("No es un numero magico")
