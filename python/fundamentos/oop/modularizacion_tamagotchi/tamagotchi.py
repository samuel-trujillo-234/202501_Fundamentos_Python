class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=100, energia=100):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        print(f"{self.nombre} jugo y ahora tiene {self.felicidad} de felicidad y {self.salud} de salud.")

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print(f"{self.nombre} comio y ahora tiene {self.felicidad} de felicidad y {self.salud} de salud.")

    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        print(f"{self.nombre} fue curado y ahora tiene {self.salud} de salud y {self.felicidad} de felicidad.")


class Dragoncito(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)
        self.salud = 150  
        self.felicidad = 120

    def lanzar_fuego(self):
        print(f"{self.nombre} lanzo fuego y quemo todo ")