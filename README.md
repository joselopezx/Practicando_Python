## Leer datos de CSV
## Leer Excel
Para leer ub excel es necesario importar pandas

import pandas as pd

pd.read_excel(nombre del archivo o ruta)

pd.head(variable donde se guardo el data frame)

pd.ExcelFile(variable donde se guardo el data frame).sheet_names // devuelve el nombre de las hojas del excel

