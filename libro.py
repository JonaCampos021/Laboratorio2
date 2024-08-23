class Libro:
    # Definición de la clase llamada libro

    def __init__(self, titulo, autor, genero, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cantidad = cantidad
    #definimos el init para crear una instancia para que se inicien los atributos del objeto

    
    def mostrar_informacion(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Cantidad en Inventario: {self.cantidad}")
    #definimos los datos que se mostraran

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        print(f"Cantidad actualizada a: {self.cantidad}")
    #definimos para actualizar la cantidad de libros que esten existente

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    cantidad = int(input("Ingrese la cantidad disponible en inventario: "))
    
    nuevo_libro = Libro(titulo, autor, genero, cantidad)
    return nuevo_libro
#definimos una función para agregar un nuevo libro


def gestion_inventario():
    inventario = []

    while True:
        print("\n--- Gestión de Inventario de Librería ---")
        print("1. Agregar un nuevo libro")
        print("2. Mostrar información de todos los libros")
        print("3. Actualizar la cantidad de un libro")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            libro = agregar_libro()
            inventario.append(libro)
            print("Libro agregado al inventario.")

        elif opcion == "2":
            if len(inventario) == 0:
                print("No hay libros en el inventario.")
            else:
                for libro in inventario:
                    libro.mostrar_informacion()

        elif opcion == "3":
            titulo = input("Ingrese el título del libro a actualizar: ")
            encontrado = False
            for libro in inventario:
                if libro.titulo == titulo:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    libro.actualizar_cantidad(nueva_cantidad)
                    encontrado = True
                    break
            if not encontrado:
                print("Libro no encontrado en el inventario.")

        elif opcion == "4":
            print("Saliendo del sistema de gestión de inventario.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        #definimos una función principal para que se pueda manejar el inventario de los libros de manera ordenada


gestion_inventario()
#se crea una instancia para llamar al metodo dentro de la clase


