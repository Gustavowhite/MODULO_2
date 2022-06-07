# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 18:41:06 2022

@author: KENDO KAPONI
"""

# Date of student
# Name: GUSTAVO BLANCO JARAMILLO
# ID: 502603
# gustavoj.blanco@upb.edu.co
# TALLER_2_MODULO_2


# se import las librerias que se van a trabajar en el proyecto

import pandas as pd
import random 
import numpy as np 

# leemos el archivo plano que tenemos en la carpeta y que se llama netflix_titles

my_datos = pd.read_csv('netflix_titles.csv')

# se imprime por consola las primeras 8 y últimas 5 filas del arreglo.

print(my_datos.head(8))

print(my_datos.tail(5))

# imprimimos los cada uno de los datos asociados a las etiquetas

print(my_datos.dtypes)

# en este punto pasamos a realizar lo que nos piden en el punto 4 del ejercio que
# es guardar un archivo.xlsx, en el cual el nombre del archivo sea “Netflix_list” 
# y el nombre de la hoja sea “títulos”.

my_datos.to_excel("Netflix_list.xlsx", sheet_name="titulos", index=(False))

# se crea un nueva Dataframe de segmente únicamente:el type, duration, la descrition and country.

my_news_datos = my_datos.loc[:,['type', 'duration', 'description', 'country']]

# the camp with time in numbers de each film

my_datos["duraciones"] = pd.to_numeric(my_datos['duration'].replace('([^0-8]*)','', regex=True), errors='coerce')

# Este codigo nos permite realizar un filtro para las películas que tienen
# una duración superior a 100 min

the_movies1_100 = my_datos[my_datos['type'].str.contains('Movie', na=False)]
movies_100_min = the_movies1_100[the_movies1_100['duraciones']>100]


# este codigo nos va a permitir que haga un filtro para los “TV Shows” que tienen más de 3 temporadas.

the_tv_show1 = my_datos[my_datos['type'].str.contains('TV Show', na=False)]
the_tv_show_3_seasons= the_tv_show1[the_tv_show1['duraciones']>3]



# aqui nos permite el codigo que solo tenga dos categorias/etiquetas y filtre elecciones
# Recuerde usar casos con indexación numérica y con texto (loc / iloc).
categorias = my_datos.loc[my_datos['listed_in'].isin(['Documentaries','International TV Shows, TV Dramas, TV Mysteries'])]

# Modifique los valores del ID de las 5 primeras y las 5últimas“shows” y 
#de cualquier otra etiqueta de su elección (solo un valor).

my_datos.iloc[:5,0]='s1'
the_tv_show1.loc[2676:,'listed_in']='Comedies, Horror Movies'

# se añade una nueva columnac “Visto”, en la cual debe colocar1/0(aleatorio)
# si vio o no el show(simulación).

my_datos["Visto"] = np.random.randint(0, 2, my_datos.shape[0])

