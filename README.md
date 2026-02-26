## Leer datos de CSV
## Leer Excel
Para leer ub excel es necesario importar pandas

import pandas as pd

pd.read_excel(nombre del archivo o ruta)

pd.head(variable donde se guardo el data frame)

pd.ExcelFile(variable donde se guardo el data frame).sheet_names // devuelve el nombre de las hojas del excel

para abrir una hoja en especifico
pd.read_excel(nombre archivo, sheet_name="nombre de hoja")

variable.tail()

variable.sample(numero de datos aleatorios)

parametro cols (rango) // en formato de excel ejp A:F

nrows para obtener solo un numero especifo de filas

##Parametros del grafico
*set_tietle* ingresa una cadena para añadirla como titulo
*set_tick_params* parametros para los tick de un eje
*figure* contenedor para el grafico como paramentros tiene (figsize = (#, #))
###PLOT
*lw* espesura de la linea del grafico
*marker* marcadores para cada punto en el plano ejemp: 'o', 'x'
### Parametros X
**tick** se refiere a las etiquetas en los ajes
*set_xlabel* ingresa una cadena para mostrar descripcion de datos en eje X
*xaxis.set_tick_params* parametros para los ticks del eje X
### Parametros Y
*set_ylabel* ingresa una cadena para mostrar descripcion de datos en eje Y
*yaxis.set_tick_params* parametros para los ticks del eje Y

## Documentación
https://pandas.pydata.org





