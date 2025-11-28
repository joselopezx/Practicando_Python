manzanas = int(input("Digite la cantidad de manzanas vendidas : "))
platanos = int(input("Digite la cantidad de plátanos vendidos : "))

if platanos>manzanas :
    print("Los plátanos tuvieron mas ventas")
elif platanos==manzanas:
    print("Hubo un empate")
else:
    print("Las manzanas tuvieron mas ventas")