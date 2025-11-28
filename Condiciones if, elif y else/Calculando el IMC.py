peso = int(input("Ingrese su peso en kilogramos (KM) : "))
altura = float(input("Ingrese su altura en metors (m) : "))

imc = peso/(altura)**2

print(f"Su IMC es : {imc:.2f}")

if imc<18.5:
    print("Por debajo del peso")
elif 18.5<=imc and imc<25:
    print("Tene peso normal")
else:
    print("Por encima del peso")