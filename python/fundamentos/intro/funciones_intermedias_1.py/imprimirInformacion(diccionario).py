def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items(): 
        print(f"{len(lista)} {clave.upper()}")  #city
        for valor in lista:  
            print(valor)  #food


costa_rica = {
    "ciudades": ["San Jose", "Limon", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}


imprimirInformacion(costa_rica)