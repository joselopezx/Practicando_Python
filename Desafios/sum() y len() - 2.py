'''
Con los mismos datos de sum() y len(), determina cuántas compras se realizaron 
por encima de 3000 reales y calcula el porcentaje con respecto al total de compras.
'''
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
gastosMin3000 = []

for gasto in gastos:
    if gasto >= 3000:
        gastosMin3000.append(gasto)

numElemetosMin3000 = len(gastosMin3000)
numeroElementosGastos = len(gastos)

porcentaje = (100*numElemetosMin3000)/numeroElementosGastos

print(f"El porcentaje de gastos mayores a 3000 con respecto a todos los gastos es : \n{porcentaje}%")