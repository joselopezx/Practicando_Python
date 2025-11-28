"""
André está probando una nueva función en el backend de Buscante que 
procesa datos en un bucle. Durante las pruebas, se dio cuenta de que 
el sistema dejó de responder y sospecha que el problema está en un bucle infinito.
¿Cuál es el problema del código de André y cómo resolverlo?
"""
#El blucle while no tiene una forma de salir del bucle, 
#esta evaluando contador < 10 pero, contador nunca incrementa
contador = 0

while contador < 10:
    print("Procesando datos...")
    contador = contador + 1