from tamagotchi import Tamagotchi

class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        self.tamagotchi.jugar()
        print(f"{self.nombre} jugo con {self.tamagotchi.nombre}")

    def darle_comida(self):
        self.tamagotchi.comer()
        print(f"{self.nombre} alimento a {self.tamagotchi.nombre}")

    def curarlo(self):
        self.tamagotchi.curar()
        print(f"{self.nombre} curo a {self.tamagotchi.nombre}")
