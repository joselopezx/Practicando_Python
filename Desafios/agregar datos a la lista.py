'''
Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: [1, 4, 7, 2, 4].
'''
listaNumeros=[]
for i in range (0,5):
    listaNumeros.append(int(input("Ingresa un numero para agregarlo a la lista : ")))
print("La lista es : ",listaNumeros)