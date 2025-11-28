"""
Estás desarrollando un sistema de control de inventario para Buscante. 
Uno de los requisitos es verificar la cantidad de ejemplares de un libro 
en inventario y continuar vendiendo hasta que el inventario se agote. 
Siempre que se realiza una venta, el sistema debe informar al usuario y 
actualizar la cantidad disponible.

Crea un programa que simule las ventas de un libro con el inventario inicial 
de 5 ejemplares. El programa debe mostrar el mensaje "¡Venta realizada! 
Inventario restante: <cantidad>" con cada venta y, al final, mostrar el mensaje 
"Inventario agotado".
"""
inventario = 5

while inventario>0:
    print(f"¡Venta realizada! Inventario restante: {inventario}")
    inventario-=1
print("Inventario agotado")