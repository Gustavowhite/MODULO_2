# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:49:39 2022

@author: KENDO KAPONI
"""


# Date of student
# Name: GUSTAVO BLANCO JARAMILLO
# ID: 502603
# gustavoj.blanco@upb.edu.co
# TALLER_3_MODULO_2


# Usando la información de cada uno de sus compañeros, cree un DataFrame en el
# cuál muestre: Nombre, edad, sexo, peso, altura, dinero a invertir, interés anual, años
# de inversión, numero de teléfono, hora de compra del pan después de
# horneado.


import numpy as np
import pandas as pd
from datetime import datetime

# en este array de DataFrame vamos a ingresar the name, edades, sexo, peso, altura, dinero a ivertir, 
# intereses anuales, años de inversion, numero de telefono, compara del pan despues de hornear
#

the_dates = pd.DataFrame({'NAMES':['ALVARO ZAMORA', 'ADRIANA SUAREZ', 'ANGELA POSSO ',' MIGUEL FABRIS', 
                                   'JHONNIER TERAN', 'ELSY SALGADO', 'GABRIELA TORREZ', 'WENDY MENDOZA', 
                                   'JESUS PORTILLO', 'DAYAN ALZATE', 'IVAN PALENCIA','GUSTAVO BLANCO', 
                                   'NOIBER BARROSO','JHONY MELENDEZ', 'DEIMER MORELO', 'JHONATAN BRITO', 
                                   'DEISON TUIRAN', 'JAIDER ECHEVERI'],
                          'AGES':[21, 23, 32, 24, 25, 26, 27, 18, 29, 30, 31, 22, 33, 34, 35, 36, 17, 28],
                          'SEX':['M ', 'F ', 'F ', 'M ', 'M ', 'F ', 'F ', 'F ', 'M ', 'M ', 'M ', 'M ', 
                                  'M ','M ', 'M ', 'M ', 'M ', 'M '],
                          'PESOS':[67, 60, 71, 52, 69, 61, 74, 78, 80, 68, 77, 74, 73, 63, 64, 65, 59, 70],
                          'HEIGHTS':[161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 
                                     175, 176, 177, 178],
                          'INVESTED_MONEY':[1200000, 1100000, 1300000, 1400000, 1500000, 1600000, 1700000, 
                                            1800000, 1900000, 2000000, 2100000, 2200000, 2300000, 2400000, 
                                            2500000, 2400000,3000000, 3100000],
                          'INTERESES_YEARS':[0.10, 0.12, 0.013, 0.014, 0.015, 0.06, 0.017, 0.18, 0.19, 0.10, 
                                             0.11, 0.12, 0.13, 0.014, 0.015, 0.016, 0.017, 0.018],
                          'YEARS_INVERTION':[1, 3, 1, 2, 1, 2, 3, 1, 4, 1, 1, 2, 3, 4, 1, 2, 1, 3],
                          'NUMBER_PHONE':['3102451200', '3242456877', '3150214522', '3105874569', 
                                          '3120251478', '3210258745', '3215743698', '3224857465', 
                                          '3231547895', '3226985477', '3172583698', '3214587866', 
                                          '3134896574', '3150213587', '3146872058', '3161587465', 
                                          '3148746598', '3170287934'],
                          'TIME_PAID_PAN':['06:00:34', '07:20:77', '08:10:16', '09:00:43', '10:21:88', 
                                           '11:30:12', '12:40:45', '13:19:11', '14:12:01', '15:05:02', 
                                           '16:10:09', '17:17:06', '18:45:04', '19:23:47', '20:24:67', 
                                           '21:00:16', '21:30:56', '22:00:00']})


# EJERCICIOS....
# • Ejercicio 1
#
# A partir de la tabla, usando el peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal de cada individuo y lo almacene en
# una variable, Muestre por pantalla la frase “Tu índice de masa corporal
# es <imc>” donde <imc> es el índice de masa corporal calculado
# redondeado con dos decimales.


# determinamos el indice de masa corporar de cada una de los integrantes que estan en 
# el dataframe y nos muestra el dato por medio de un print...

for i in the_dates.index:
    imc = round(((the_dates["PESOS"][i])/((the_dates["HEIGHTS"][i])/100)),2)
    print(""" HELLO, {} tus indices de masa corporar esta en:  {} """.format(str(the_dates["NAMES"][i]),str(imc)))



# • Ejercicio 2
# A partir de los datos recolectados: Escribir un programa que teniendo en
# cuenta una cantidad a invertir, el interés anual y el número de años,
# muestre por pantalla el capital obtenido en la inversión.

# muestra el numero de años invertidos, cantidad invertida


for i in the_dates.index:
    capital_obtenido = round(the_dates["INVESTED_MONEY"][i]*(((the_dates["INTERESES_YEARS"][i])/(100+1))**the_dates["YEARS_INVERTION"][i]),2)
    print("""HELLO, {} el capital obtenido en la inversión {}""".format(str(the_dates["NAMES"][i]),str(capital_obtenido)))



# • Ejercicio 3
# Una panadería vende barras de pan a $15,000 COP cada una. El pan
# tiene un descuento del 10%, 20%, 30%, 40%, cuando no se vende en las
# primeras 6h, 12h, 18h, 24h, después de horneado. Crear una columna
# en el DataFrame para determinar el porcentaje de descuento obtenido
# de acuerdo a la hora en que fue realizada la compra. Y otra columna
# para el precio final obtenido.


# para este ejercicio vamos a pensar que la hora de hornear se realiza a las 3:30 de la mañana
# y que ademas el precio del pan en esta panaderia es de 14 mil pesos "14000"



the_dates["HOURS_DESP_HORNEADO"] = ((pd.to_timedelta(the_dates["TIME_PAID_PAN"])-pd.to_timedelta("03:30:23")).dt.total_seconds())//3600


condition = [
    (the_dates ["HOURS_DESP_HORNEADO"] >= 0) & (the_dates["HOURS_DESP_HORNEADO"] <6),
    (the_dates ["HOURS_DESP_HORNEADO"] >= 6) & (the_dates ["HOURS_DESP_HORNEADO"] <12),
    (the_dates ["HOURS_DESP_HORNEADO"] <= 12) & (the_dates ["HOURS_DESP_HORNEADO"] <18),
    (the_dates ["HOURS_DESP_HORNEADO"] <= 18) & (the_dates ["HOURS_DESP_HORNEADO"] <24)]
select = [2, 4, 6, 8]


the_dates["THE_DESCUENT"] = np.select(condition, select, default='not it requiered')
the_dates["FINAL_PRICE"] = 14000-(pd.to_numeric(the_dates["THE_DESCUENT"], errors='coerce') * 14000)



# • Ejercicio 4
# Los teléfonos de sus compañeros tienen el siguiente formato prefijonúmero-extensión
# donde el prefijo es el código del país +57, y la
# extensión tiene dos dígitos (por ejemplo +57-913724710-##). Debe
# organizar en el DataFrame (nueva columna) las extensiones de forma
# que si el sexo de la persona es M, debe poner como extensión 11 y si el
# sexo es F, debe poner como extensión 10.



# aqui vamos a determinar una condition que nos determine que cuando sea M nos relaciones 
# with el numero 11 y cuando sea F nos la relacione con el numero 10

condition_real = [
    (the_dates ["SEX"] == "M"),
    (the_dates ["SEX"] == "F")]
selection_real = [11, 10]


the_dates["Extension_phone"] = np.select(condition_real, selection_real, default='not it requiered')

