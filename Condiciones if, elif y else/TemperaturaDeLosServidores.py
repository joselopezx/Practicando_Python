#ingresar la temperatura del servidor
temperaturaServidor = int(input("Ingrese la temperatura del servidor: "))
if temperaturaServidor>25:
    print("¡Alerta! Temperatura por encima del limite permitido")
else:
    print("Temperatura normal")