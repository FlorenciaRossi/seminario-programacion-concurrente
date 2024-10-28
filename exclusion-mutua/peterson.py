import threading
import time

flag = [False, False]  
turn = 0    

def proceso_0():
    global turn
    flag[0] = True  # P0 quiere entrar a la sección crítica
    turn = 1  # Cede el turno a P1

    # Espera activa
    while flag[1] and turn == 1:
        pass  

    # Sección crítica
    print("Proceso 0: Entrando a la sección crítica.")
    time.sleep(1)  
    print("Proceso 0: Saliendo de la sección crítica.")

    # Sale de la sección crítica
    flag[0] = False

def proceso_1():
    global turn
    flag[1] = True  # P1 quiere entrar a la sección crítica
    turn = 0  # Cede el turno a P0

    # Espera activa
    while flag[0] and turn == 0:
        pass  

    # Sección crítica
    print("Proceso 1: Entrando a la sección crítica.")
    time.sleep(1)  
    print("Proceso 1: Saliendo de la sección crítica.")

    # Sale de la sección crítica
    flag[1] = False



hilo_0 = threading.Thread(target=proceso_0)
hilo_1 = threading.Thread(target=proceso_1)

hilo_0.start()
hilo_1.start()

hilo_0.join()
hilo_1.join()

print("Los procesos terminaron.")