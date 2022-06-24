# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:23:16 2022

@author: KENDO KAPONI
"""


# Date of student
# Name: GUSTAVO BLANCO JARAMILLO
# ID: 502603
# gustavoj.blanco@upb.edu.co
# TALLER_8_MODULO_2_HW_ARBOL_DE_DECISION


# PRIMERO DETERMINAMOS LAS LIBRERIAS PARA CASO DE ARBOLES DE DECISIONES

import numpy as np
import pandas as pd
import pydotplus
import matplotlib.image as pltimg
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier


carseats = sm.datasets.get_rdataset("Carseats", "ISLR") 
datos = carseats.data
print(carseats.__doc__)

datos['ventas_altas'] = np.where(datos.Sales > 8, 0, 1)
datos = datos.drop(columns = 'Sales')



dc1= {'Yes':1, 'No':0}
dc2= {'the_Bads':1, 'the_Mediums':2, 'the_Goods':3}
datos["Urban"] = datos["Urban"].map(dc1)
datos["US"] = datos["US"].map(dc1)
datos["ShelveLoc"] = datos["ShelveLoc"].map(dc2)

# caracteristicas del dataFrame de cada nombre de la columna de la base de dato

caract = ["CompPrice","Income","Advertising", "Population","Price","ShelveLoc","Age","Education","Urban","US"]

# declaracion de varibles dependientes and independ

x = datos[caract]
y = datos["ventas_altas"]

# ahora procedemos con el Train y el test de la regresion 

# the part the train

x_train = x[:300]
y_train = y[:300]

# test

x_test = x[300:]
y_test = y[300:]


dtc_tree = DecisionTreeClassifier()
dtc_tree = dtc_tree.fit(x_train, y_train)

the_predictions = dtc_tree.predict([[120, 60, 12, 112, 152, 2, 44, 18, 3, 5]])


dat = tree.export_graphviz(dtc_tree, out_file=None, feature_names=caract)
graphic = pydotplus.graph_from_dot_data(dat)
graphic.write_png('mydecisiontree.png')
imgs = pltimg.imread("mydecisiontree.png")
implot = plt.imshow(imgs)
plt.show()





