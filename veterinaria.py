class Veterinaria:
    #creamos una clase que la llamaremos veterinaria
    
    def __init__(self, peso=0, nombre="", clase="", color="", edad=0, genero=""):
        self.Estado = "NO ATENDIDO"
        self.peso = peso
        self.tamano = self.determinar_tamano()
        self.Nombre = nombre
        self.Clase = clase  
        self.Color = color
        self.Edad = edad
        self.Genero = genero
    #a partir de aqui definimos la funcion y agregamos los datos que se usaran

    def determinar_tamaño(self):
        if self.peso <= 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"
    #determinamos el tamaño del perro por medio del def y utilizamos el if para saber si el perro el grande o pequeño

    def cambiar_estado(self):
        self.Estado = "ATENDIDO"
        return self.Estado
    #definimos por medio del def que despues de ingresar los datos del estado del perro pase a se atendido
    

    def entrada_datos(self):
        self.Nombre = input("Nombre del Perro: ")
        self.Clase = input("Ingrese qué raza es su mascota: ")
        self.Color = input("Ingrese el color de su mascota: ")
        self.Edad = int(input("Ingrese la edad de su mascota: "))
        self.peso = int(input("Ingrese el peso de su mascota en kg: "))
        self.Genero = input("Ingrese el género de su mascota: ")
        self.tamano = self.determinar_tamano()  
    #aqui definimos los datos que el usuario ingresara
        
    def muestra_datos(self):
        print(f"Nombre: {self.Nombre}")
        print(f"Raza: {self.Clase}")
        print(f"Color: {self.Color}")
        print(f"Edad: {self.Edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamano}")
        print(f"Género: {self.Genero}")
        print(f"Estado: {self.Estado}")
    #definimos la funcion oara que muestre los datos que han sido ingresados

perro = Veterinaria()  
perro.entrada_datos()  
perro.cambiar_estado()  
perro.muestra_datos()  
#se crean instancias para llamar a los metodos dentro de las clases
