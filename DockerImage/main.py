import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,calinski_harabasz_score,classification_report,confusion_matrix
import warnings
from requests import get

warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn.cluster._kmeans")
warnings.filterwarnings("ignore", category=UserWarning, module="joblib.externals.loky.backend.context")

# read data
ENDPOINT = "https://wine-data.onrender.com/wine"
response = get(ENDPOINT)
df_wine=pd.datos = pd.read_json(response.json())
print('')
print("cantidad de filas: " + str(df_wine.shape[0]))
print("cantidad de columnas: " + str(df_wine.shape[1]))
print('')
# cantidad de nulos
print('')
print ("cantidad de valores nulos: " + str(df_wine.isna().sum().sum()))

#parametros correlacionados
def calcular_y_mostrar_correlacion(df):
    # Calcular la matriz de correlación
    matriz_correlacion = df.corr()

    # Inicializar una lista para almacenar los pares (índice, columna, valor)
    pares_correlacion = []

    # Recorrer la matriz de correlación
    for indice_fila_1 in matriz_correlacion.index:
        for indice_columna_1 in matriz_correlacion.columns:
            valor_correlacion_1 = matriz_correlacion.loc[indice_fila_1, indice_columna_1]

            # Evaluar la condición (mayor a 0.5)
            if abs(valor_correlacion_1) > 0.5 and abs(valor_correlacion_1) < 1.0:

                # Verificar si ya existe un par con los mismos elementos en la lista
                existe_par = False
                for par in pares_correlacion:
                    indice_fila_2, indice_columna_2, valor_correlacion_2 = par
                    if (indice_fila_1 == indice_fila_2 and indice_columna_1 == indice_columna_2) or \
                       (indice_fila_1 == indice_columna_2 and indice_columna_1 == indice_fila_2):
                        existe_par = True
                        break

                # Si no existe un par con los mismos elementos, agregar a la lista
                if not existe_par:
                    pares_correlacion.append([indice_fila_1, indice_columna_1, valor_correlacion_1])

    # Imprimir los pares de columnas y sus valores de correlación
    print('')
    print("Pares de columnas con correlación mayor a 0.5 (excluyendo 1.0):")
    for par in pares_correlacion:
        print(f"{par[0]} - {par[1]}: {par[2]}")

# Ejemplo de uso con tu DataFrame df_wine
calcular_y_mostrar_correlacion(df_wine)

#Escalado de datos
scaler=StandardScaler()
X=scaler.fit_transform(df_wine)

#modelo clustering Kmeans
k = 3
km = KMeans(n_clusters=k, random_state=0)
km.fit(X)
df_wine_label=df_wine.copy()
# Agregar una nueva columna 'Cluster' al DataFrame original
labels_kmeans= km.labels_
df_wine_label['Cluster'] = labels_kmeans 
df_wine_label_gropued=df_wine_label.groupby('Cluster').mean()
print('')
print(df_wine_label_gropued)
