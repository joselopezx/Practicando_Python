"""
José está desarrollando una funcionalidad en el sistema de Buscante 
para interrumpir la búsqueda tan pronto como se encuentre un libro específico. 
La lista de libros ya registrados en el sistema es la siguiente:
Ayuda a José a crear un programa que recorra la lista y muestre el mensaje 
"Libro encontrado: <nombre del libro>" tan pronto como se encuentre el libro "El Hobbit". 
Después de encontrar el libro, el programa debe detener inmediatamente la búsqueda, 
sin verificar los libros restantes.
"""
libros = ["1984", "Cien años de soledad", "El Principito", "El Hobbit", "Orgullo y Prejuicio"]
libroABuscar = "El Hobbit"
for libro in libros:
    if libro == libroABuscar:
        print(f"Libro encontrado: {libro}")
        break
