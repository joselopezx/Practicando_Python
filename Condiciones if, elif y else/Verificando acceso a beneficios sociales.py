ingresos = float(input("Ingresos percibidos : "))
cantidadHijos = int(input("Cuantos hijos tiene? "))

if ingresos<=2000 and cantidadHijos>=1:
    print("Tiene derecho a beneficio")
else:
    print("No tiene derecho a beneficio")