import pandas as pd

media_emision_gas = pd.DataFrame({
'Año':[1970, 1970, 1970, 1971, 1971, 1971, 1972, 1972, 1972],
'Gas':['C2F6 (t)', 'CF4 (t)', 'CH4 (t)', 'C2F6 (t)', 'CF4 (t)', 'CH4 (t)', 'C2F6 (t)', 'CF4 (t)', 'CH4 (t)'], 
'Emisión': [0.232610, 3.557421, 1471.024024, 0.33461, 5.1173, 1525.5, 0.40468,6.18902,1584.7195]
})

print(media_emision_gas)

media_emision_gas = media_emision_gas.pivot_table(values = 'Emisión', index = 'Gas', columns = 'Año')

print(media_emision_gas)