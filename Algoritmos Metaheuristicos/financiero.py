import random as rd
import pandas as pd
import math
import numpy as np

# --- CONFIGURACIÓN DEL MERCADO ---
ACTIVOS = ["Acciones Tech", "Bonos", "Cripto", "Oro"]
RETORNOS = np.array([0.8, 0.8, 0.8, 0.8])
VOLATILIDAD = np.array([0.20, 0.2, 0.20, 0.2])
N_ACTIVOS = len(ACTIVOS)

# --- PARÁMETROS WOA ---
N_BALLENAS = 30
LIMITE_INF, LIMITE_SUP = 0, 1  # Pesos entre 0% y 100%
N_ITERACIONES = 50
B = 1

def inicializarBallena():
    # Genera una lista de pesos aleatorios para los N activos
    pesos = [round(rd.uniform(LIMITE_INF, LIMITE_SUP), 2) for _ in range(N_ACTIVOS)]
    return np.array(pesos)

def fitnes(pesos):
    # Normalizamos para que sumen 1 (100%)
    if sum(pesos) == 0: return 1e6
    w = pesos / sum(pesos)
    
    retorno_p = np.sum(w * RETORNOS)
    riesgo_p = np.sum(w * VOLATILIDAD)
    
    sharpe_ratio = retorno_p / riesgo_p
    return -sharpe_ratio # Negativo porque el código busca el MINIMO

# Inicialización
ballenas = [inicializarBallena() for _ in range(N_BALLENAS)]

# --- CICLO DE OPTIMIZACIÓN ---
for iteracion in range(N_ITERACIONES):
    fitnesBallenas = [fitnes(b) for b in ballenas]
    
    # Encontrar al líder (el mejor Sharpe Ratio)
    mejor_idx = fitnesBallenas.index(min(fitnesBallenas))
    mejor_ballena = ballenas[mejor_idx].copy()
    
    a = 2 - iteracion * (2 / N_ITERACIONES)
    a2 = -1 + iteracion * (-1 / N_ITERACIONES) # b_linear del original

    for i in range(N_BALLENAS):
        p = rd.random()
        l = (a2 - 1) * rd.random() + 1
        A = 2 * a * rd.random() - a
        C = 2 * rd.random()

        if p < 0.5:
            if abs(A) < 1:
                # Moverse hacia el líder
                D = abs(C * mejor_ballena - ballenas[i])
                ballenas[i] = mejor_ballena - A * D
            else:
                # Exploración aleatoria
                X_rand = rd.choice(ballenas)
                D = abs(C * X_rand - ballenas[i])
                ballenas[i] = X_rand - A * D
        else:
            # Trayectoria en espiral
            D_prima = abs(mejor_ballena - ballenas[i])
            ballenas[i] = D_prima * math.exp(B * l) * math.cos(l * 2 * math.pi) + mejor_ballena
        
        # Límites de seguridad [0, 1]
        ballenas[i] = np.clip(ballenas[i], LIMITE_INF, LIMITE_SUP)

# --- RESULTADOS FINALES ---
mejor_final = ballenas[fitnesBallenas.index(min(fitnesBallenas))]
pesos_optimos = mejor_final / sum(mejor_final)

print(f"--- RESULTADOS TRAS {N_ITERACIONES} ITERACIONES ---")
for nombre, peso in zip(ACTIVOS, pesos_optimos):
    print(f"{nombre}: {round(peso*100, 2)}%")

print(f"\nMejor Sharpe Ratio (Negativo): {round(min(fitnesBallenas), 4)}")