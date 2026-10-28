import numpy as np
import pandas as pd
# Johan Paulo Aros NC 0016
## datos natriz 4 x 3
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
# y almacenar la tabla en la variable df dataframe
print("---Datos a partir de una matriz 4 x 3 ---")
df=pd.DataFrame(datos_alumno,columns=['ci','marcas','paquetes'])
print(df)
# datos a partir de un diccionario
print("---Datos a partir de un diccionario---")
alumno_diccionario={
    "nombre":["Johan","Ricardo","Alan","Cris","Iram","Scar"],
    "califa":[100,90,100,80,70,50],
    "edad":[15,15,16,16,18,20]
}

estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Johan Paulo Aros NC 0016")