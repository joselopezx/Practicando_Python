import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('inmigrantes_canada.csv')
print(df.head())
print(df.shape)
print(df.info())

print('====== PAISES COMO INDICE =======')
df.set_index('Pais', inplace= True)
print(df.head())

anios = list(map(str, range(1980, 2014)))
print(f'================= ANIOS ===========\n{anios}')

colombia = df.loc['Colombia', anios]
print(f'======== DATOS COLOMBIA =======\n{colombia}')

colom_dict = {'Año' : colombia.index.tolist(), 'Inmigrantes' : colombia.values.tolist()}

datos_colom = pd.DataFrame(colom_dict)
print(f'====== DF COLOMBIA INMIGRANTES =====\n{datos_colom.tail()}')

plt.figure(figsize=(12, 5))
plt.plot(datos_colom['Año'], datos_colom['Inmigrantes'])
plt.xticks(['1980', '1985','2010','2000'])
plt.title('Inmigracion de colombianos hacia Canada')
plt.xlabel('Año')
plt.ylabel('Numero de inmigrantes')
plt.show()

#////////////////////////////////
fig, ax = plt.subplots(figsize = (8, 4))
ax.plot(datos_colom['Año'],datos_colom['Inmigrantes'])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Inmigracion de colombianos hacia canada \n 1980 - 2013')
ax.set_xlabel('Año')
ax.set_ylabel('Numero de inmigrantes')
plt.show()

fig, axs = plt.subplots(1,2,figsize=(10, 4))
axs[0].plot(datos_colom['Año'], datos_colom['Inmigrantes'])
axs[0].set_title('Inmigrantes de colombianos hacia canada')
axs[0].set_xlabel('Año')
axs[0].set_ylabel('Numero de inmigrantes')
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
#plt.grid() para añadir cuadricula al grafico

axs[1].boxplot(datos_colom['Inmigrantes'])
axs[1].set_title('Boxplot de la inmigracion de colombianos \n hacia Cadana 1980 - 2013')
axs[1].set_xlabel('Colombia')
axs[1].set_ylabel('Numero de inmigrantes')
plt.show()

print(datos_colom.describe())

fig, subg = plt.subplots(2,2,figsize=(12, 8))
fig.subplots_adjust(hspace=0.5, wspace=0.3)
fig.suptitle('Inmigracion de paises sudamericanos \n hacia Canada de 1980 a 2013')

subg[0,0].plot(df.loc['Colombia', anios])
subg[0,0].set_title('Colombia')

subg[0,1].plot(df.loc['Brasil', anios])
subg[0,1].set_title('Basil')

subg[1,0].plot(df.loc['México', anios])
subg[1,0].set_title('México')

subg[1,1].plot(df.loc['Perú', anios])
subg[1,1].set_title('Perú')

ymin = 0
ymax = 7000

for ax in subg.ravel():
    ax.set_ylim(ymin, ymax)

for ax in subg.flat:
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    ax.set_xlabel('Año')
    ax.set_ylabel('Numero de inmigrantes')
    ax.grid()

plt.show()