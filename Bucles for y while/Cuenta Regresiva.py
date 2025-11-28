"""
Aline está implementando una funcionalidad que muestra mensajes 
personalizados para los clientes durante una promoción especial 
de su nueva librería. El sistema debe mostrar un mensaje de cuenta 
regresiva personalizado para cada número de 10 a 1, y al final mostrar 
el mensaje: "¡Aprovecha la promoción ahora!".

Crea un programa que utilice un bucle for para mostrar los siguientes mensajes:

Para números pares, muestra: "Faltan solo <número> segundos - ¡No pierdas esta oportunidad!".
Para números impares, muestra: "La cuenta continúa: <número> segundos restantes.".
Al final de la cuenta, muestra el mensaje: "¡Aprovecha la promoción ahora!".
"""

numero = 10

while numero > 0:
    if (numero%2)==1:
        print(f"La cuenta contunúa : {numero} segundos restantes")
    else:
        print(f"Faltan solo {numero}, segundos restantes")
    numero-=1
print("¡Aprovecha la promoción ahora!")

"""
for segundos in range(10, 0, -1):  
    if segundos % 2 == 0: 
        print(f"Faltan solo {segundos} segundos - ¡No pierdas esta oportunidad!")
    else: 
        print(f"La cuenta continúa: {segundos} segundos restantes.")

print("¡Aprovecha la promoción ahora!")
"""