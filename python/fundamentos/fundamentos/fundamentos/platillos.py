platillos_tipicos = {"México": "Tacos", "Colombia": "Ajiaco", "Costa Rica": "Casado"}

#Otra forma de iterar a través de las claves

for clave in platillos_tipicos.keys():

    print(clave)

#Imprime: México, Colombia, Costa Rica

#Iteramos a través de los valores

for valor in platillos_tipicos.values():

    print(valor)

#Imprime: Tacos, Ajiaco, Casado

#Iteramos a través de los elementos (clave-valor)

for clave, valor in platillos_tipicos.items():

    print(clave, "=", valor)

#Imprime: México = Tacos, Colombia = Ajiaco, Costa Rica = Casado
