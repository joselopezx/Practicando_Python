import pandas as pd

# Creando el DataFrame con las informaciones
datos = pd.DataFrame({
    'Fecha de venta': ['01/01/2022', '05/02/2022', '10/03/2022', '15/04/2022','18/04/2022','20/04/2022'],
    'valor': [100, 150, 200, 250,80,180]
})

# Mostrando el DataFrame
print(datos)

datos['Fecha de venta'] = pd.to_datetime(datos['Fecha de venta'], format=f'%d/%m/%Y')
print(datos, datos.info())
