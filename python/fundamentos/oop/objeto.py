class Perro:
    def __init__(self, nombre, edad, raza):
        #Dentro del codigo del constructor vamoos a definir el estado
        #inicial de cualquier perro que sea creado
        self.name = nombre
        self.age = edad
        self.race = raza

    def cumple(self):
        self.age += 1

    def getName(self):
        return self.name
    
    

miperro = Perro("Bobby", 5, "Poodle")

#print("El nombre de mi perro es", miperro.getName())