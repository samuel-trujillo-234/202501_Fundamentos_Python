def valores_multiplicados_segundo(lista):
    if len(lista) < 2: 
        print(len(lista))  
        return []  
    
    segundo_valor = lista[1]  
    nueva_lista = [x * segundo_valor for x in lista]  
    
    print(len(nueva_lista)) 
    return nueva_lista

resultado1 = valores_multiplicados_segundo([1, 3, 5, 7])  
print(resultado1)

resultado2 = valores_multiplicados_segundo([1]) 
print(resultado2)