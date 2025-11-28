#definir funcion para evaluar los dias
def diasNegativos(dias):
    if dias < 0:
        return True
    else:
        return False

diasTotales = 0
#uso del for para ongresar solo tres dias sin repetir codigo
for tarea in range (0,3):
    dias = int(input("Ingrese los dias para realizar la actividad : "))
    #evaluacion y llamada a la funcion para saber si los dias son negativos 
    if diasNegativos(dias):
        print("Error: los días no pueden ser negativos")
        diasTotales=("Ingresaste dias negativos")
        break
    diasTotales+=dias
print("Dias totales : ", diasTotales)