# Alicia está observando el crecimiento de la población de Águas de San Pedro, 
# un acogedor pueblo ubicado en el interior de San Pablo.
# Debido a los análisis que ha estado realizando, ha estado buscando algunas 
# formas de representar visualmente la tendencia del crecimiento poblacional a lo largo del tiempo 
# y ha decidido trazar un gráfico de líneas, porque, vamos a admitirlo, los gráficos son una forma 
# muy buena de contar historias con números.

# Afortunadamente, ya tiene todo lo que necesita: un DataFrame almacenado en una variable 
# llamada df_aguas, que contiene el número de habitantes en la columna n_habitantes 
# y los años en la columna ano

import pandas as pd
import matplotlib.pyplot as plt

df_aguas = pd.DataFrame({'ano': [1970, 1980, 1991, 2000, 2010, 2020],
                         'n_habitantes': [830, 1091, 1697, 1883, 2703, 3500]})

plt.plot(df_aguas['ano'], df_aguas['n_habitantes'])
plt.show()