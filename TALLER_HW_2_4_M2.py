# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 18:27:01 2022

@author: KENDO KAPONI
"""
# Date of student
# Name: GUSTAVO BLANCO JARAMILLO
# ID: 502603
# gustavoj.blanco@upb.edu.co
# TALLER_4_MODULO_2



# comenzanmos importando las librerias que se requieren para este 
# ejercicio

import pandas as pd
from sklearn import linear_model
import numpy as np

# aqui procedemos a importar la base de datos que vamos a trabajar

auto_df = pd.read_csv('cars.csv')

the_condition = [
    (auto_df["Car"] == "Toyoty"),
    (auto_df["Car"] == "Mitsubishi"),
    (auto_df["Car"] == "Skoda"),
    (auto_df["Car"] == "Fiat"),
    (auto_df["Car"] == "Mini"),
    (auto_df["Car"] == "VW"),
    (auto_df["Car"] == "Mercedes"),
    (auto_df["Car"] == "Hyundai"),
    (auto_df["Car"] == "Ford"),
    (auto_df["Car"] == "Audi"),
    (auto_df["Car"] == "Suzuki"),
    (auto_df["Car"] == "Honda"),
    (auto_df["Car"] == "Hundai"),
    (auto_df["Car"] == "Opel"),
    (auto_df["Car"] == "BMW"),
    (auto_df["Car"] == "Mazda"),
    (auto_df["Car"] == "Volvo"),
    ]
the_selections = [3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 7.5, 8.0, 9.0, 9.5, 10.0, 10.5, 12.5, 13.0, 15.5, 17.5]

auto_df["Estad_Cars"] = np.select(the_condition, the_selections, default='Not Specified')
pd.to_numeric(auto_df["Estad_Cars"])



# ahora pasamos a determinar las variables independientes 

x = auto_df[["Volume","Weight","CO2"]]

# AHORA DETERMINAMOS LA VARIABLE DEPENDIENTE

y = auto_df["Estad_Cars"]

# aqui se realiza un proceso de rgression con el codigo Linear....

mod_regre = linear_model.LinearRegression()
mod_regre.fit(x, y)

# aqui con el .predit se esta la prediccion del co2

the_predi_of_CO2 = mod_regre.predict([[2500,790,99]])
print(f"la prediction de CO2 es de: {the_predi_of_CO2}")
print(f"El modelo de regresion es de: {mod_regre.coef_} ")



