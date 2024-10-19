import threading
import time
import random

# Semaphore.acquire decrementa  el valor en uno. Si el sem es > 0 puede avanzar, sino se bloquea (wait).
# Semaphore.release incrementa el valor en uno (signal).
N = 5
contador = 0
contadorLibre = threading.Semaphore(1)  
avanzarTodos = threading.Semaphore(0)        

def proceso(id):
    global contador

    print(f"Proceso {id}: ejecutando código antes de la marca.")
    time.sleep(random.uniform(0.1, 2.0))
    
    # Encuentro    
    contadorLibre.acquire()
    contador += 1
    if contador == N:
        avanzarTodos.release()  
    contadorLibre.release()

    # esperar que todos lleguen
    avanzarTodos.acquire()
    avanzarTodos.release()


    time.sleep( random.uniform(0.1, 2.0))
    print(f"Proceso {id}: terminó su ejecución.")


hilos = []
for i in range(N):
    hilo = threading.Thread(target=proceso, args=(i,))
    hilos.append(hilo)
    hilo.start()


for hilo in hilos:
    hilo.join()

print("Todos los procesos han terminado.")
