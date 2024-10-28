import threading
import time
variable_global = 0

lock = threading.Lock()

def critical_section(thread_id):
    global variable_global

    print(f"hilo {thread_id} entro a la seccion critica")
    valor_antiguo = variable_global
    time.sleep(2)
    variable_global = valor_antiguo + 1
    print(f"hilo {thread_id} esta actualizando el valor de {valor_antiguo} a {variable_global}")
    print(f"hilo {thread_id} esta dejando la seccion critica")

cant_hilos = 5

hilos = []

for i in range(cant_hilos):
    t = threading.Thread(target=critical_section, args=(i,))
    hilos.append(t)
    t.start()

for i in hilos:
    i.join()
    
print(f"valor final del recurso compartido: {variable_global}")
        