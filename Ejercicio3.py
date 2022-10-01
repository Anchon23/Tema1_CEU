lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []
lista_3_0 = []
for i in lista_1:
    for j in lista_2:
        if i == j:
            lista_3.append(i)
    lista_3 = list(tuple(lista_3))
for item in lista_3:
    if item not in lista_3_0:
        lista_3_0.append(item)
print(lista_3_0)