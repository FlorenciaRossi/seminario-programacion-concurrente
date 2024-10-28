import threading
import time

# Variables compartidas
banderas = [0, 0]  # Indica si cada proceso quiere entrar a la región crítica
turno = 0  # Define de quién es el turno para entrar

def proceso(elemento, iteraciones):
    global banderas, turno

    for _ in range(iteraciones):
        banderas[elemento] = 1  # El proceso indica que quiere entrar

        # Espera activa si el otro proceso también quiere entrar y no es su turno
        while banderas[1 - elemento] == 1 and turno != elemento:
            pass  # Espera activa

        # Región crítica
        print(f'Proceso {elemento + 1} en la región crítica...')
        time.sleep(1)  # Simula trabajo en la región crítica
        print(f'Termino proceso {elemento + 1}\n')

        # Ceder el turno al otro proceso
        turno = 1 - elemento
        banderas[elemento] = 0  # El proceso deja de indicar que quiere entrar

def iniciar(num_iteraciones):
    # Crear los hilos para ambos procesos
    t1 = threading.Thread(target=proceso, args=(0, num_iteraciones))
    t2 = threading.Thread(target=proceso, args=(1, num_iteraciones))

    # Iniciar los hilos
    t1.start()
    t2.start()

    # Esperar a que ambos procesos terminen
    t1.join()
    t2.join()

# Ejecutar el algoritmo con 5 iteraciones por proceso
iniciar(5)
