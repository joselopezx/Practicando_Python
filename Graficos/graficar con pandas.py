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