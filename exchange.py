from threading import Thread
import time

comun = 1

def proceso(nombre):
    local = 0
    while True:
        print(f"PROCESO {nombre} FUERA DE LA ZONA CRITICA")
        time.sleep(0.5)
        while True:
            global comun
            comun, local = local, comun
            if local == 1:
                break
        time.sleep(0.5)
        print(f"PROCESO {nombre} ENTRO A LA SECCIOON CRITICA")
        comun, local = local, comun

p = Thread(target=proceso, args=("PRIMERO",))
q = Thread(target=proceso, args=("SEGUNDO",))

p.start()
q.start()