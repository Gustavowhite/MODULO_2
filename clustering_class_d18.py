# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 08:58:44 2022

@author: KENDO KAPONI
"""

# importamos las librerias 

import numpy as np
from sklearn import linear_model

# vamos a generar o creamos los datos de pruebas
# X reprrsentar el tamoño del tumor en cm 
# Y hacemos reshape para cambiar de filas a columnas para que pueda funcionar
# la regresion logistrica

X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 
       4.96, 4.52, 3.69, 5.88]).reshape(-1,1)

# y represeta si el tumor es canceroso o no - 1 si - 0 no

y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

#  creamos el modelo de regresion logistica

log_reg_model = linear_model.LogisticRegression()
log_reg_model.fit(X,y)

# predecir si un tumor con cierto tamaño es canceroso o no.
predict_tumor = log_reg_model.predict(np.array([3.46]).reshape(-1,1))

# imprimir la prediccion
print(predict_tumor)

# creamos funciones de probabilidad para verificar que dado un tamaño del tumor
# nos diga que tan probable es que sea canceroso

def log_reg_prob(log_reg_model,X):
    log_odds = log_reg_model.coef_*X+log_reg_model.intercept_
    odds = np.exp(log_odds)
    probability = odds/(1 + odds)
    return(probability)
    

print(log_reg_prob(log_reg_model, X))












