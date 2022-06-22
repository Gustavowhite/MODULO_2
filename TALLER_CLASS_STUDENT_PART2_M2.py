# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 20:17:40 2022

@author: KENDO KAPONI
"""



# first import the libraris that be to need

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler


# importamos la base de datos estudiante que vamos a trabajar

stdent_df = pd.read_csv('student_data.csv')

# primero seleccionamos las dos variables independients

x_stdent = stdent_df[["age", "famrel"]]

# despues seleccionamos la variable dependiente

y_stdent = stdent_df["Walc"]


# ahora pasamos a la estandarizacion de la variable

scale_stdent = StandardScaler()
scale_x_stdent = scale_stdent.fit_transform(x_stdent)


# ahora procedemos con el Train y el test de la regresion 

# the part the train

x_train_stdent = scale_x_stdent[:80]
y_train_stdent = y_stdent[:80]

# and the part the test

x_test_stdent = scale_x_stdent[80:]
y_test_stdent = y_stdent[80:]


# now to going with the part the el modelo regresion multiples

mode_stdent = linear_model.LinearRegression()
mode_stdent.fit(x_train_stdent, y_train_stdent)

# pasamos a la prediccion del modelo

predi_scale_x_stdent = mode_stdent.predict([x_test_stdent[0]])
print(f"la prediccion del modelo es de: {predi_scale_x_stdent}")

# ahora determinamos la relacion de train y test

# this is for the train

r2_train = r2_score(y_train_stdent, mode_stdent.predict(x_train_stdent))
print(f"el R de la relacion del train es de: {r2_train:.4f}")

# this is for the test

r2_test = r2_score(y_test_stdent, mode_stdent.predict(x_test_stdent))
print(f"el R de la relacion del test es de:{r2_test:.4f} ")














