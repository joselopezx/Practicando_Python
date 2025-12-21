'''
Escribe una función que genere la tabla de multiplicar de un número 
entero del 1 al 10, según la elección del usuario. Como ejemplo, 
para el número 7, la tabla de multiplicar se debe mostrar en el siguiente formato:
# Tabla del  7:
# 7 x 0 = 0
# 7 x 1 = 7
# [...]
# 7 x 10 = 70
'''

def tablaMult (numero):
    for i in range (1,11):
        print(f"{numero} * {i} = {numero*i}")

numero = int(input("Ingrese el numero a multiplicar : "))
tablaMult(numero)