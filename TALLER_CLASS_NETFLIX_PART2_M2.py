# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 21:27:26 2022

@author: KENDO KAPONI

"""




# Date of student
# Name: GUSTAVO BLANCO JARAMILLO
# ID: 502603
# gustavoj.blanco@upb.edu.co
# TALLER_7_MODULO_2_ regresion de NETFLIX


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler


# IMPORTAMOS LA BASE DE DATOS A TRABAJAR PARA ESTE CASO 

netf_df = pd.read_excel('Netflix_list.xlsx')

netf_df["duracion"] = pd.to_numeric(netf_df['duration'].replace('([^0-9]*)', '', regex=True), errors='coerce')


the_conditions = [
    (netf_df["type"] == "TV Show"),
    (netf_df["type"] == "Movie")
    ]
the_selections = [1.0, 2.0]
netf_df["Cod_type"] = np.select(the_conditions, the_selections, default= 'NOT requerid')

the_condition1 = [
    (netf_df["duration"].str.contains("min").astype(np.bool_)),
    (netf_df["duration"].str.contains("Season").astype(np.bool_))
    ]
the_seleccion1 = [1.0, 2.0]
netf_df["duration_type"] = np.select(the_condition1, the_seleccion1, default='NOT requierid')

# Variables independient
x_netf = netf_df[["Cod_type","duration_type"]][:2500] 


# determinamos la variable dependient

y_netf = netf_df["duracion"][:2500]

# ahora pasamos a la estandarizacion de la de la variable

scale_netf = StandardScaler()
scale_x_netf = scale_netf.fit_transform(x_netf)

# ahora procedemos con el Train y el test de la regresion 

# the part the train

x_train_netf = scale_x_netf[:2000]
y_train_netf = y_netf[:2000]

# and the part the test

x_test_netf = scale_x_netf[2000:]
y_test_netf = y_netf[2000:]



# now to going with the part the el modelo regresion multiples


mode_netf = linear_model.LinearRegression()
mode_netf.fit(x_train_netf, y_train_netf)


# pasamos a la prediccion del modelo

predi_scale_x_netf = mode_netf.predict([x_test_netf[0]])
print(f"la prediccion del modelo es de: {predi_scale_x_netf} ")

# ahora determinamos la relacion de train y test

# this is for the train

r2_train = r2_score(y_train_netf, mode_netf.predict(x_train_netf))
print(f"el R de la relacion del train es de: {r2_train:.4f}")

# this is for the test

r2_test = r2_score(y_test_netf, mode_netf.predict(x_test_netf))
print(f"el R de la relacion del test es de:{r2_test:.4f} ")





