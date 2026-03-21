import random as rd
import pandas as pd
import math

N_BALLENAS = 20
LIMITE_INF, LIMITE_SUP = -10, 10
N_ITERACIONES = 20
B = 1

df = pd.DataFrame()

def inicializarBallena():
    return round(rd.uniform(LIMITE_INF, LIMITE_SUP),2)

def fitnes(x):
    return x**2

ballenas = []
for i in range (N_BALLENAS):
    ballenas.append(inicializarBallena())

df['Ballena Inicial'] = ballenas


for iteracion in range (N_ITERACIONES):
    fitnesBallenas = [fitnes(b) for b in ballenas]
    mejor_fitnesID = fitnesBallenas.index(min(fitnesBallenas))
    mejor_fitnes = ballenas[mejor_fitnesID]
    for i in range(N_BALLENAS):
        
        a = 2 - iteracion * (2/N_ITERACIONES)
        a2 = 2 - iteracion * (-1 / N_ITERACIONES)

        A = 2 * a * rd.random() - a
        C = 2 * rd.random()

        l = (a2 - 1) * rd.random() + 1

        p = rd.random()
        if p < 0.5 : 
            if abs(A) < 1:
                #Actualizar posicion del agente de busqueda actual
                #Update Position of Current Search Agent
                D = abs(C * mejor_fitnes - ballenas[i])
                ballenas[i] = mejor_fitnes - A * D
            else: # abs(A) >= 1
                X_rand = rd.choice(ballenas)
                D = abs(C * X_rand - ballenas[i])
                ballenas[i] = X_rand - A * D
        else:
            D_prima = abs(mejor_fitnes - ballenas[i])
            ballenas[i] = D_prima * math.exp(B * l) * math.cos(l * 2 * math.pi) + mejor_fitnes
        if ballenas[i] < LIMITE_INF: ballenas[i] = LIMITE_INF
        if ballenas[i] > LIMITE_SUP: ballenas[i] = LIMITE_SUP

fitnesFinal = [fitnes(b) for b in ballenas]

df['Ballena final'] = [round(b, 4) for b in ballenas]
df['Fitnes'] = [round(f, 4) for f in fitnesFinal]

print(f'---------- NUMERO ITERACIONES ---------\n{N_ITERACIONES}')
print(df)