# Trabajas como Analista de Datos en una empresa minorista y 
# te asignaron la tarea de crear una figura con subgráficos que muestre 
# la variación en el número de ventas en cuatro tiendas diferentes a lo largo de un año. 
# La gerencia de la empresa necesita visualizar claramente las tendencias de ventas en cada tienda, 
# para que puedan tomar decisiones estratégicas sobre inventarios y acciones de marketing. 
# Para ello, debes crear cuatro subgráficos dispuestos en dos filas y dos columnas,
# donde cada subgráfico represente una tienda diferente. En este desafío, 
# cada subgráfico debe presentar un gráfico de líneas que muestre la variación del 
# número de ventas a lo largo de los meses del año.

import pandas as pd
import matplotlib.pyplot as plt

# DATA FRAME 
tiendas = ['A', 'B', 'C', 'D']
ventas_2022 = {'Ene': [100, 80, 150, 50],
    'Feb': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'May': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Sep': [240, 160, 290, 130],
    'Oct': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dec': [300, 350, 400, 250]}

df = pd.DataFrame(ventas_2022, index=tiendas)
print(f'========= DATA FRAME =========\n {df.head()} {df.info()}')

fig, subg = plt.subplots(2,2,figsize=(14,8))
plt.subplots_adjust(wspace=0.3, hspace=0.4)
fig.suptitle('Ventas en el periodo de enero a diciembre 2022 en las tiendas')

subg[0,0].plot(df.loc['A'])
subg[0,0].set_title('Ventas tienda A')

subg[0,1].plot(df.loc['B'])
subg[0,1].set_title('Ventas tienda B')

subg[1,0].plot(df.loc['C'])
subg[1,0].set_title('Ventas tienda C')

subg[1,1].plot(df.loc['D'])
subg[1,1].set_title('Ventas tienda D')

for ax in subg.flat:
    ax.set_xlabel('Mes')
    ax.set_ylabel('Ventas')

ymin = 0
ymax = 400

for ax in subg.ravel():
    ax.set_ylim(ymin, ymax)

plt.show()