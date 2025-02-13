from persona import Persona
from tamagotchi import Tamagotchi
from tamagotchi import Dragoncito

tama = Tamagotchi("Tama", "Rojo")
persona1 = Persona("Gon", "Killua", tama)

persona1.darle_comida()
persona1.curarlo()
persona1.jugar_con_tamagotchi()

dragon = Dragoncito("Draco", "Negro")
persona2 = Persona("Carlos", "López", dragon)

persona2.darle_comida()
persona2.jugar_con_tamagotchi()
dragon.lanzar_fuego()