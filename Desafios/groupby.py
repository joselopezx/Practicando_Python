import pandas as pd

df = pd.DataFrame({
   'Animal': ['Perro', 'Gato', 'Elefante', 'Perro', 'Gato', 'Elefante'],
   'Color': ['Negro', 'Blanco', 'Gris', 'Marrón', 'Negro', 'Marrón'],
   'Cantidad': [2, 3, 1, 4, 2, 2]
})

print(df)

print("====== AGRUPAR POR 'ANIMAL' ======")
print(df.groupby('Animal').sum(numeric_only=True))

print("====== AGRUPAR POR DOS COLUMNAS 'ANIMAL y COLOR' ======")
print(df.groupby(['Animal', 'Color'])[['Cantidad']].sum())