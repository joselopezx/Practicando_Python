'''
    Verifica si la base de datos contiene datos nulos y, en caso de tenerlos, 
    realiza el tratamiento de estos datos nulos de la manera que consideres más coherente con la situación.

    Los estudiantes "Alicia" y "Carlos" ya no forman parte del grupo. Por lo tanto, 
    elimínalos de la base de datos.

    Aplica un filtro que seleccione solo a los estudiantes que fueron aprobados.

    Guarda el DataFrame que contiene solo a los estudiantes aprobados en un archivo CSV llamado 
    "alumnos_aprobados.csv".

    Extra: Al revisar las calificaciones de los estudiantes aprobados, 
    notamos que algunas calificaciones eran incorrectas. 
    Las estudiantes que obtuvieron una calificación de 7.0, 
    en realidad tenían un punto extra que no se contabilizó.
    Por lo tanto, reemplaza las calificaciones de 7.0 en la base de datos por 8.0. 
    Consejo: busca el método replace.

'''

import pandas as pd

link = "https://gist.githubusercontent.com/ahcamachod/807a2c1cf6c19108b2b701ea1791ab45/raw/fb84f8b2d8917a89de26679eccdbc8f9c1d2e933/alumnos.csv"

df = pd.read_csv(link)

print(f"<<<<<<<<<<< DATOS ORIGINALES >>>>>>>>>>\n {df}")

print(f"<<<<<<<<<<< DATOS FALTANTES >>>>>>>>>>>\n {df.isnull().sum()}")

df = df.fillna(0)
print(f"<<<<<<<<<<< TRATAMIENTO DE DATOS >>>>>>>>>>\n {df}")

consultaNombres = df.query("Nombre == 'Alicia' | Nombre == 'Carlos'").index
df.drop(consultaNombres, axis=0, inplace=True)

print(f"<<<<<<<<<<< ELIMINANDO DEL DF A ESTUDIANTES >>>>>>>>>>\n {df}")

aprobados = df.query("Nota >= 6")
print(f"<<<<<<<<<<<< ALUMNOS APROBADOS >>>>>>>>>>>>\n {aprobados}")

df["Nota"]=df["Nota"].replace(7.0, 8.0)

aprobados = df.query("Nota >= 6")
print(f"<<<<<<<<<<<< ALUMNOS APROBADOS >>>>>>>>>>>>\n {aprobados}")

df.to_csv("Nuevo data frame", sep=";", index=False)