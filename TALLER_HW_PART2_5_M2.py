# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:30:27 2022

@author: KENDO KAPONI
"""


# Date of student
# Name: GUSTAVO BLANCO JARAMILLO
# ID: 502603
# gustavoj.blanco@upb.edu.co
# TALLER_5_MODULO_2



# 1.Descargue la base de datos de: https://archive.ics.uci.edu/ml/datasets/Air+Quality#
# 2.Seleccione las parejas x y del dataset para utilizarlos en una regresiónlineal y polinomial.
# 3.Grafique el diagrama de dispersión
# 4.Verifique elrde relación
# 5.Las variables escogidas son libres.

# para este ejercicio menzamos con las librerias

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score
from sklearn import linear_model

# primero vamos a proceder a importar la base de los datos
# a trabajar en un archivo .xlsx desde un archivo csv

# *********** VAMOS CON UNA REGRESION LINEAL****

df = pd.read_excel('AirQualityUCI.xlsx')

x = df["CO(GT)"]
y = df["NOx(GT)"]

pendient,interc,rel,p,err_stand = stats.linregress(x,y)

def regresion(x):
    return pendient*x + interc

mode = list(map(regresion, x))

plt.scatter(x,y)
plt.plot(x, mode)
plt.show()


#  ********** se realiza una prediccion

predicr_linl = regresion(5)
print(f"se pudo predecir que la prediccion de la regresion lineal es: {predicr_linl:5f} y el rel de la relacion es de: {rel:5f} ")

#  ***************     REGRESION POLINOMIAL

# ahora vamos a realizar una regresion polinimial

mode_poli = np.poly1d(np.polyfit(x,y, 3))

poli_lineal = np.linspace(1,25,100)

poli_new_y = mode_poli(poli_lineal)

plt.scatter(x,y)
plt.plot(poli_lineal, poli_new_y)
plt.show()

#Prediccion
predicr_poli = mode_poli(5)
rel2_poli = r2_score(y,mode_poli(x))
print(f"para este caso nos arroja que la regresion polinomial es de {predicr_poli:5f} y el rel2 de la relacion es de {rel2_poli:5f} ")


# *****************  REGRESION MULTIPLE

# ahora aplicamos los mismos casos, pero en una regresion multiple para ver que nos arroja

# para este caso de la regresion multiple pues vamos a tomar la primera variable que tomamos en la 
# la regresion lineal.

reg_m = df[["CO(GT)"]]

reg_model = linear_model.LinearRegression()
reg_model.fit(reg_m,y)

#Prediccion 
predi_mult = reg_model.predict([[5]])
rel3_mult = reg_model.coef_
print(f"se estimo que la prediccion de la regresion Multiple es de: {predi_mult} y el rel de relacion es de: {rel3_mult} ")




