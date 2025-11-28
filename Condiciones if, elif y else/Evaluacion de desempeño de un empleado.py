puntuacionDesempenio = int(input("Ingrese el desempeño del empleado (escala de 0 - 10)"))
aniosTrabajados = int(input("Ingrese los años trabajados del empleado"))
if puntuacionDesempenio<7:
    print("Necesita mejorar")
elif aniosTrabajados<=5:
    print("Necesita mejorar")
else:
    print("Elegible para ascenso")