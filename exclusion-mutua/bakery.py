import threading
import time

cant_hilos = 5

variable_global = 0
number = [0] * cant_hilos  # Array que guarda los turnos de cada thread 
choosing = [False] * cant_hilos  # Flags para indicar que un thread esta eligiendo su numero

def obtener_max():   # Funcion para retornar el mayor número en el array number.
    return max(number)

def bakery_lock(thread_id):
    global number, choosing

    choosing[thread_id] = True # Indica que el thread esta eligiendo su numero 
    number[thread_id] = 1 + obtener_max()  
    choosing[thread_id] = False # Termina de elegir su numero 

    for j in range(cant_hilos):    # Esperar a que los demas threads obtengan su número y respetar el turno
        if j == thread_id:
            continue             # Saltar la comparación consigo mismo
        while choosing[j]:    # Esperar a que el otro thread termine de elegir su numero
            pass            # Mantenerse en este bucle mientras el otro thread esta eligiendo
        while number[j] != 0 and (number[j], j) < (number[thread_id], thread_id):  # Esperar a que los threads con numeros mas bajos (o igual número y menor ID) terminen
            pass

def bakery_unlock(thread_id):
    global number
    number[thread_id] = 0 # Libera el turno

def critical_section(thread_id):
    global variable_global

    bakery_lock(thread_id)

    print(f"Hilo {thread_id} entró a la sección crítica")
    valor_antiguo = variable_global
    time.sleep(1)  
    variable_global = valor_antiguo + 1
    print(f"Hilo {thread_id} está actualizando el valor de {valor_antiguo} a {variable_global}")
    print(f"Hilo {thread_id} salió de la sección crítica")
    
    bakery_unlock(thread_id)

hilos = []
for i in range(cant_hilos):
    t = threading.Thread(target=critical_section, args=(i,))
    hilos.append(t)
    t.start()


for t in hilos:
    t.join()

print(f"Valor final del recurso compartido: {variable_global}")
