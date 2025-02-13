def sumatoria_menos_longitud(numeros):
    suma = sum(numeros) 
    longitud = len(numeros) 
    return suma - longitud 

# Prueba
resultado = sumatoria_menos_longitud([1, 2, 3, 4]) 
print(resultado) 
