# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 08:47:31 2022

@author: KENDO KAPONI
"""

# Date of student
# Name: GUSTAVO BLANCO JARAMILLO
# ID: 502603
# gustavoj.blanco@upb.edu.co
# TALLER_6_MODULO_2_of_the_11_of_junio_regresion.


# Bueno lo primero que importamos son las librerias y que nos piden o las que 
# vamos requiriendo 

import pandas as pd 
from sklearn import linear_model
#import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
#import numpy as np

# Aqui cargamos los datos de archivo plano o un.csv donde vamos a encontrar 
# distintas variables 

cars2_df = pd.read_csv("cars2.csv")


# variable independiente de la base de datos

x_cars2 = cars2_df[['Weight', 'Volume']]

# variable dependiente de la base datos

y_cars2 = cars2_df[['CO2']]

# procedemos a realizar la estandaration de la variable indenpent

scaler_cars2 = StandardScaler()
scale_x_cars2 =scaler_cars2.fit_transform(x_cars2)


# train / test 

x_train_cars2 = scale_x_cars2[:20]
y_train_cars2 = y_cars2[:20]

x_test_cars2 = scale_x_cars2[20:]
y_test_cars2 = y_cars2[20:]

# ahora vamos aplicar el modelo de ********regresion multiple*****

mode_regre_cars2 = linear_model.LinearRegression()
mode_regre_cars2.fit(x_train_cars2 ,y_train_cars2)


# ahora pasamos hacer una ******prediccion del modelo****

predic_scale_xcars2 = mode_regre_cars2.predict([x_test_cars2[0]])
print(f" la prediccion del modelo es de: {predic_scale_xcars2} ")

# ahora viene el R de relacion train

r2_cars2_train = r2_score(y_train_cars2, mode_regre_cars2.predict(x_train_cars2))
print(f" El r de relacion train es de: {r2_cars2_train}")

# or print(r2_cars2_train)

# ahora viene el R de relacion test

r2_cars2_test = r2_score(y_test_cars2, mode_regre_cars2.predict(x_test_cars2))
print(f"el R de relacion test es de: {r2_cars2_test}")


# or tambien se puede imprimir de esta manera: print(r2_cars2_test)




