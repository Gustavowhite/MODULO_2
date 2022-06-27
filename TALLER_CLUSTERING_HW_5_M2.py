# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:28:30 2022

@author: KENDO KAPONI
"""

# Date of student
# Name: GUSTAVO BLANCO JARAMILLO
# ID: 502603
# gustavoj.blanco@upb.edu.co
# TALLER_HW_5_MODULO_2_ULTIMO TALLER DE CLUSTERS

# tarea de clustering
# enviar resultado por git hub

# REALIZAMOS LAS IMPORTACIONES DE LAS LIBRERIAS A TRABAJAR

import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs


# Gráficos
# ********** -------- *********
# ********** estas librerias nos va a permitir mostrar las graficas de lo ******
# ********** de las distintos datos a tratar en el modelo clustering      ******


import matplotlib.pyplot as plt
from matplotlib import style     # nos permite mostrar las graficas
style.use('ggplot') or plt.style.use('ggplot')

# Preprocesado y modelado 
# estas son las librerias de procesamiento y modelado de los datos
# ==============================================================================
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
from sklearn.preprocessing import scale
from sklearn.metrics import silhouette_score

# Configuración warnings
# este preparacion del warnings es para que emita mensajes de alerta, 
# en este caso el programa va a filtar todas la advertencias y las va a ignorar
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')


def plot_dendrogram(model, **kwargs):
    '''
    Esta función extrae la información de un modelo AgglomerativeClustering
    y representa su dendograma con la función dendogram de scipy.cluster.hierarchy
    '''
    
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot
    dendrogram(linkage_matrix, **kwargs)
    
    
    
    # Simulación de datos 
    # aqui en la simulacion de datos lo que realiza el programa es 
    # es separar los datos en 4 grupos distinto donde la separacion 
    # con un acercamiento de los datos hacia cada grupo.
# ==============================================================================

# el metodo make_blobs simula los datos donde para este caso tiene 
#  200 puntos en la grafica y en cuatro centroides o grupos distribuidos.
X, y = make_blobs(
        n_samples    = 200, 
        n_features   = 2, 
        centers      = 4, 
        cluster_std  = 0.60, 
        shuffle      = True, 
        random_state = 0
       )

# en esta parte lo que muestra es la grafica con la ubicacion de los puntos
# en las coordenadas x y y ademas, los ayuda a diferenciar con la ayudas de 
# colores recorriendo un bucle en cada una de los grupos.

fig, ax = plt.subplots(1, 1, figsize=(6, 3.84))
for i in np.unique(y):
    ax.scatter(
        x = X[y == i, 0],
        y = X[y == i, 1], 
        c = plt.rcParams['axes.prop_cycle'].by_key()['color'][i],
        marker    = 'o',
        edgecolor = 'black', 
        label= f"Grupo {i}"
    )
ax.set_title('Datos simulados')
ax.legend();

# Escalado de datos
# ==============================================================================
X_scaled = scale(X)



# Modelos
# aqui se implementos los modelos de los datos para este caso serian tres
# y que sus linkage son complete, average y ward y por ultimo con medidas 
# euclesianas diferentes
# ==============================================================================
modelo_hclust_complete = AgglomerativeClustering(    # entremientos de datos
                            affinity = 'euclidean',
                            linkage  = 'complete',
                            distance_threshold = 0,
                            n_clusters         = None   # el n_clusters genera
                                                        # el numero de cluster
                        )
modelo_hclust_complete.fit(X=X_scaled)

modelo_hclust_average = AgglomerativeClustering(
                            affinity = 'euclidean',
                            linkage  = 'average',
                            distance_threshold = 0,
                            n_clusters         = None
                        )
modelo_hclust_average.fit(X=X_scaled)

modelo_hclust_ward = AgglomerativeClustering(
                            affinity = 'euclidean',
                            linkage  = 'ward',
                            distance_threshold = 0,
                            n_clusters         = None
                     )
modelo_hclust_ward.fit(X=X_scaled)


# Dendrogramas 
# aqui se observan los tres dendogramas de los tres modelos para este caso 
# de los datos
# ==============================================================================
fig, axs = plt.subplots(3, 1, figsize=(8, 8))
plot_dendrogram(modelo_hclust_average, color_threshold=0, ax=axs[0])
axs[0].set_title("Distancia euclídea, Linkage average")
plot_dendrogram(modelo_hclust_complete, color_threshold=0, ax=axs[1])
axs[1].set_title("Distancia euclídea, Linkage complete")
plot_dendrogram(modelo_hclust_ward, color_threshold=0, ax=axs[2])
axs[2].set_title("Distancia euclídea, Linkage ward")
plt.tight_layout();




fig, ax = plt.subplots(1, 1, figsize=(8, 4))
altura_corte = 6
plot_dendrogram(modelo_hclust_ward, color_threshold=altura_corte, ax=ax)
ax.set_title("Distancia euclídea, Linkage ward")
ax.axhline(y=altura_corte, c = 'black', linestyle='--', label='altura corte')
ax.legend();


# Método silhouette para identificar el número óptimo de clusters
# ==============================================================================

# *****************************************
#aqui se determina o se encuentra el numero optimos de clustering 
# despues de encontrar el numero mas optimo para la muestra y que para este
#ejemplo se trabaja de 2 a 15 cluster, pero antes de modela los datos apartir
# de un bucle for, donde los resultados se van guardando en una varible para 
# determinar el valor mas optimo y despues se muestra en un grafico utizando 
#linkage
# *************************************************

range_n_clusters = range(2, 15)
valores_medios_silhouette = []

for n_clusters in range_n_clusters:
    modelo = AgglomerativeClustering(
                    affinity   = 'euclidean',
                    linkage    = 'ward',
                    n_clusters = n_clusters
             )

    cluster_labels = modelo.fit_predict(X_scaled)
    silhouette_avg = silhouette_score(X_scaled, cluster_labels)
    valores_medios_silhouette.append(silhouette_avg)
    
fig, ax = plt.subplots(1, 1, figsize=(6, 3.84))
ax.plot(range_n_clusters, valores_medios_silhouette, marker='o')
ax.set_title("Evolución de media de los índices silhouette")
ax.set_xlabel('Número clusters')
ax.set_ylabel('Media índices silhouette');


# Modelo
# luego de todo el procedimiento del las variables del clusters se 
# se escoge para este caso el linkage ward con determinacion de cluster
# apropiado de 4 para la muestra de los datos en las grafica que lo 
# muestra el 4 en el eje x y en el eje y esta en el punto 0.65
# ==============================================================================
modelo_hclust_ward = AgglomerativeClustering(
                            affinity = 'euclidean',
                            linkage  = 'ward',
                            n_clusters = 4
                     )
modelo_hclust_ward.fit(X=X_scaled)

print(n_clusters)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    