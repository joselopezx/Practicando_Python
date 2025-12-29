'''
    Identificar qué hacer durante un proceso de análisis exploratorio;
    Calcular el promedio de valores de un DataFrame;
    Agrupar los datos según una columna específica utilizando groupby;
    Realizar selecciones utilizando el método query;
    Transformar Series en DataFrames;
    Ordenar valores de un DataFrame con sort_values;
    Graficar barras verticales y horizontales;
    Visualizar valores únicos con unique;
    Utilizar value_counts para contar valores únicos y calcular porcentajes;
    Cambiar nombres de columnas.

    Cuando trabajamos con bases de datos, en ocasiones puede ser necesario cambiar los nombres de las columnas. 
    Por ejemplo, cuando creamos el siguiente DataFrame en nuestro proyecto:
    df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')

    Podemos ver que la columna con los porcentajes está nombrada como "Tipo". ¿Y si quisiéramos cambiar su nombre a "Porcentajes"?

    En ese caso, podemos utilizar el método rename() para cambiar el nombre de esa columna. Este método nos
    permite especificar un diccionario que asocia el nombre antiguo de la columna con el nuevo nombre que deseamos asignar. 
    Entonces, hagámoslo:

    # Guardando el DataFrame en una variable
    df_ejemplo = df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')

    # Cambiando el nombre de la columna "Tipo" a "Porcentajes"
    df_ejemplo.rename(columns={'Tipo': 'Porcentajes'}, inplace=True)

    # Visualizando el DataFrame
    df_ejemplo

    Hemos utilizado el parámetro inplace=True para que este cambio se aplique definitivamente en nuestro DataFrame df_ejemplo. 


'''

import matplotlib.pyplot as plt
import pandas as pd

link = "https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv"

dataSet = pd.read_csv(link, sep=";")

print(dataSet)

print(dataSet['Valor'].mean(numeric_only=True))

print(dataSet.groupby('Tipo').mean(numeric_only=True))

print(dataSet.groupby('Tipo')['Valor'].mean(numeric_only=True))

print(dataSet.groupby('Tipo')[['Valor']].mean(numeric_only=True).sort_values('Valor'))

df_tipo_precio = dataSet.groupby('Tipo')[['Valor']].mean(numeric_only=True).sort_values('Valor')
df_tipo_precio.plot(kind='barh', figsize=(12,6), color='purple')

print(dataSet.Tipo.unique())

porcentaje_tipo = dataSet.Tipo.value_counts(normalize=True).to_frame()
print(porcentaje_tipo)

tipoDepartamento = dataSet.query('Tipo == "Departamento"')
print(tipoDepartamento)
print(tipoDepartamento.head(2))


porcentaje_tipo.plot(kind='bar', figsize=(12,6), color='purple', xlabel='Tipos', ylabel='Porcentajes')


'''
    Calcular el promedio de habitaciones por departamento.

    Verificar cuántas colonias únicas existen en nuestra base de datos.

    Analizar qué colonias tienen el promedio de alquiler más alto.

    Crear un gráfico de barras horizontales que muestre las 5 colonias con los promedios de alquiler más altos.
'''
print("<<<<<<<<<<<<< DESAFIO >>>>>>>>>>>>")
print(dataSet['Habitaciones'].mean())

print(len(dataSet['Colonia'].unique()))

print(dataSet['Colonia'].nunique())

print(dataSet.groupby('Colonia')[['Valor']].mean().sort_values('Valor', ascending=False))

(dataSet.groupby('Colonia')[['Valor']].mean().sort_values('Valor', ascending=False).head()).plot(kind='barh', figsize=(12,6), color='green')
plt.show()