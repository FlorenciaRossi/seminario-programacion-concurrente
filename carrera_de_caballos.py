from threading import Thread
import time

hay_ganador = False
meta = 10
ganador = ''

class Caballo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = 0

    def correr(self):
        global hay_ganador, ganador, meta
        while(not hay_ganador):
            time.sleep(0.2)


            print("Caballo: ",self.nombre, " posicion: ", self.posicion)
            self.posicion += 1
            if (self.posicion == meta):
                hay_ganador = True
                ganador = self.nombre


def crear_carrera(n):
    hilos = list()
    for i in range(n):
        caballo = Caballo(f"{i+1}")
        hilo = Thread(target= caballo.correr)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()
    
    for hilo in hilos:
        hilo.join()


n = int(input("Ingrese una cantidad de caballos: \n"))
crear_carrera(n)
print("\nCABALLO GANADOR: ", ganador)
