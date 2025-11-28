ingresosTotales = int(input("Ingresos totales : "))
gastosTotales = int(input("Ingrese los gastos totales : "))
clientesNuevos = int(input("Ingrese la cantidad de  lientes nuevos : "))

calculo = ingresosTotales-gastosTotales

if calculo > 10000 and clientesNuevos > 50:
    print("Trimestre Exelente")
elif calculo > 5000 and clientesNuevos<=20:
    print("Triestre bueno")
elif gastosTotales > 0:
    print("Trimentre Regular")
else:
    print("Trimestre deficitario")