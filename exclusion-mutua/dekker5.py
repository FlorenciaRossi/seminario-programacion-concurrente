import threading

# Variables compartidas
turno = 1  # Indica qué proceso tiene el turno
lock = threading.Lock()  # Bloqueo para coordinar las impresiones
eventos = [threading.Event(), threading.Event()]  # Eventos para controlar los turnos

# Inicializar ambos eventos en falso
eventos[0].clear()
eventos[1].clear()

def Proceso1(num_iteraciones):
    global turno
    for _ in range(num_iteraciones):
        eventos[0].wait()  # Espera a que sea el turno del proceso 1
        eventos[0].clear()  # Consumir el evento

        # Región crítica
        with lock:
            print("Proceso 1 en la región crítica")

        # Cambio de turno
        turno = 2
        eventos[1].set()  # Despierta al proceso 2

        with lock:
            print("Proceso 1 terminó su iteración")

def Proceso2(num_iteraciones):
    global turno
    for _ in range(num_iteraciones):
        eventos[1].wait()  # Espera a que sea el turno del proceso 2
        eventos[1].clear()  # Consumir el evento

        # Región crítica
        with lock:
            print("Proceso 2 en la región crítica")

        # Cambio de turno
        turno = 1
        eventos[0].set()  # Despierta al proceso 1

        with lock:
            print("Proceso 2 terminó su iteración")

def iniciar(num_iteraciones):
    global turno

    # Crear los threads para los procesos
    t1 = threading.Thread(target=Proceso1, args=(num_iteraciones,))
    t2 = threading.Thread(target=Proceso2, args=(num_iteraciones,))

    # Iniciar los procesos alternando el turno inicial
    eventos[0].set()  # El proceso 1 comienza primero

    t1.start()
    t2.start()

    # Esperar a que ambos procesos terminen
    t1.join()
    t2.join()

# Iniciar la ejecución con 5 iteraciones por proceso
iniciar(5)

