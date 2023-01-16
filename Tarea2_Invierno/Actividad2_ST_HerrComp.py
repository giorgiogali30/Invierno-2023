print("Programa para la segunda tarea")
print("------------------------------------------------------------------------") 
import pandas as pd
df = pd.read_excel('A01657409_Registro1.xlsx')
print("Número de filas, Número de columnas: ",df.shape)
print("------------------------------------------------------------------------") 
print("Nombre de cada columna del doc:   ", df.columns)
print("------------------------------------------------------------------------")
print("Qué datos tiene cada columna: ", df.dtypes)    
print("------------------------------------------------------------------------")
print("------------------------Columna: Calorías (kcal)------------------------------------")
print("valores únicos: ", df["Calorías (kcal)"].unique()) 
print("valor max: ",df["Calorías (kcal)"].max(), "      y       valor min: ",df["Calorías (kcal)"].min())       
print("Media: ", df["Calorías (kcal)"].mean())        #promedio
print("Mediana: ",df["Calorías (kcal)"].median())      #mediana (valor que se encuentra al centro de la lista ordenada de valores)
print("Desv Est: ", df["Calorías (kcal)"].std())         #desviación estándar, qué tan dispersos están los datos alrededor de la media
print("------------------------Columna: Proteína (g)------------------------------------")
print("valores únicos: ", df["Proteína (g)"].unique()) 
print("valor max: ",df["Proteína (g)"].max(), "      y       valor min: ",df["Calorías (kcal)"].min())       
print("Media: ", df["Proteína (g)"].mean())        #promedio
print("Mediana: ",df["Proteína (g)"].median())      #mediana (valor que se encuentra al centro de la lista ordenada de valores)
print("Desv Est: ", df["Proteína (g)"].std())         #desviación estándar, qué tan dispersos están los datos alrededor de la media


