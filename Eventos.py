import threading
import time
import random

# Evento de salida
salida_event = threading.Event()

def corredor(id_corredor):
    print("Corredor " + str(id_corredor) + " en posición, esperando señal de salida...")
    # Los corredores esperan al evento
    salida_event.wait()
    # Se simula el tiempo de la carrera
    tiempo_carrera = random.uniform(1, 3)
    time.sleep(tiempo_carrera)
    print("Corredor " + str(id_corredor) + " ha llegado a la meta.")

def iniciar_carrera():
    print("Señal de salida en 2 segundos...")
    time.sleep(2)
    print("¡Salida! Los corredores han comenzado.")
    # Se activa el evento una vez se indica que los corredores han comenzado
    salida_event.set()

# Se crean los hilos que representan a cada corredor
corredores = []
for i in range(5):
    hilo = threading.Thread(target=corredor, args=(i,))
    corredores.append(hilo)
    hilo.start()

# Iniciar la carrera
iniciar_carrera()

# Se espera a que todos los hilos terminen
for hilo in corredores:
    hilo.join()