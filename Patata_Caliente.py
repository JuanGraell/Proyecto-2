import random
from classQueue import Queue

def patataCaliente(listaNombres):
    colaSimulacion = Queue()
    for nombre in listaNombres:
        colaSimulacion.enqueue(nombre)
    
    while colaSimulacion.size() > 1:
        for i in range (random.randint(1,50)):
            colaSimulacion.enqueue(colaSimulacion.dequeue())

        print(colaSimulacion.dequeue(), "se eliminó")
        
    return colaSimulacion.dequeue()

jugadores = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(patataCaliente(jugadores), "ganó")