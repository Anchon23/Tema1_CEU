from audioop import reverse
from collections import deque
from logging.config import valid_ident
from multiprocessing.sharedctypes import Value
from pickle import TRUE
cola = deque()
lista_tareas = list(cola)
diccionario = {}
while True:
    tareas = input("Introduce una tarea del proyecto: ")
    lista_tareas.append(tareas)
    prioridad = input("Introduce un numero entre el 1 y el 9 para indicar la importancia a la tarea asignada: ")
    lista_tareas.append(prioridad)
    diccionario[prioridad]=[tareas]
    acabar = input("¿Desea Introducir más tareas? (SI/NO): ")
    ordenar = sorted(diccionario.items())
    lista_tareas.sort()
    # lista_tareas.remove(prioridad)
    if acabar.upper() == "NO":
        break
# Las tareas estan ordendadas de menor a mayor
print(lista_tareas)