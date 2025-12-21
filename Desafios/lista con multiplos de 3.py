'''
 Crea una función que lea la siguiente lista y devuelva una nueva lista con los múltiplos de 3:
[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplos_de_tres(lista):
    return [num for num in lista if num % 3 == 0]

# Uso de la función
lista_original = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
mult_3 = multiplos_de_tres(lista_original)
print(mult_3)


'''
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplos3():
    multiplos = []
    for numero in lista:
        if numero % 3 == 0:
            multiplos.append(numero)
    return multiplos

print(multiplos3())