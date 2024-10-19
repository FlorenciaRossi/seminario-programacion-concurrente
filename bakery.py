# Cumple todas las condiciones
# - exclusión mutua await np = 0 or nq < np 
#     nadie le resta a np o nq
# - dead lock
from threading import Thread
import time


np = 0
nq = 0
def p():
    while True:
        time.sleep(2)
        print("Sección no critica")
        global np
        np = nq + 1
        while not(nq == 0 or np < nq):
            pass
        print("Sección critica proceso P")
        np = 0

def q():
    while True:
        time.sleep(2)
        print("Sección no critica")
        global nq
        nq = np + 1
        while not(np == 0 or nq < np):
            pass
        print("Sección critica proceso Q")
        nq = 0
    
prcP = Thread(target=p)
prcQ = Thread(target=q)

prcP.start()
prcQ.start()