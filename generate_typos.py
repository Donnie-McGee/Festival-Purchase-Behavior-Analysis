import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\PC\Desktop\Estudio\Analisis de Datos\Proyectos\Festival Purchase Behavior Analysis\festival_dataset_dirty.csv")

def insertar_malaga(df, columna='origin_city', cantidad=3721):
    # Seleccionar índices aleatorios únicos de la columna (sin importar su valor actual)
    indices_aleatorios = df.sample(n=cantidad, random_state=42).index
    
    # Reemplazar esos valores por "Malaga"
    df.loc[indices_aleatorios, columna] = 'Malaga'
    
    return df

df = insertar_malaga(df)

df.to_csv(r"C:\Users\PC\Desktop\Estudio\Analisis de Datos\Proyectos\Festival Purchase Behavior Analysis\festival_dataset_dirty.csv", index=False)