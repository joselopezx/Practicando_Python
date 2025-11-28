"""
João está desarrollando un sistema de registro para un sitio de lectura. 
Necesita asegurarse de que los usuarios ingresen un nombre de usuario y 
una contraseña válidos. Las reglas son las siguientes:

El nombre de usuario debe tener al menos 5 caracteres.
La contraseña debe tener al menos 8 caracteres.
João quiere que el sistema siga solicitando la información 
hasta que ambas condiciones se cumplan. Cuando el usuario ingresa 
datos válidos, el programa debe mostrar el mensaje: "¡Registro realizado con éxito!".
"""
while True:
    nombre = input("Ingrese el nombre : ")
    contraseña = input("Ingrese la contraseña : ")
    if len(nombre) < 5:
        print("El nombre debe de ser de al menos de 5 caracteres : ")
        continue
    if len(contraseña) < 8:
        print("La contraseña debe de ser de al menos de 8 caracteres : ")
        continue
    print("Registro Exitoso! ")
    break