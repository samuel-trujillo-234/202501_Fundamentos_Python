def iterarDiccionario2(llave, lista):
    for diccionario in lista:  
        if llave in diccionario: 
            print(diccionario[llave])  


cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]


iterarDiccionario2("nombre", cantantes)  
print("---")
iterarDiccionario2("pais", cantantes)  
