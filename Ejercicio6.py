def separar(lista):
    
    '''Funcion que contiene una lista de numeros y devuelve dos listas, una lista con todos los nummeros pares y la otra lista con todos los 
    numeros impares'''

    lista_pares = []
    lista_impares = []
    for x in numeros_enteros:
        if x % 2 == 0:
            lista_pares.append(x)
            lista_pares.sort()
        else:
            lista_impares.append(x)
            lista_impares.sort()
    return lista_pares,lista_impares

numeros_enteros = [2,5,6,9,4,1,0,3]  
lista_pares,lista_impares = separar(numeros_enteros)
print(lista_pares)
print(lista_impares)