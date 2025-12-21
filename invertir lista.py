'''
Recoge 5 números enteros e imprime la lista en orden inverso al enviado.
'''

listaNumeros = []

for i in range (0,5):
    listaNumeros.append(int(input("Ingrese un numero : ")))

print(listaNumeros[::-1])
listaNumeros.reverse()
print(listaNumeros)