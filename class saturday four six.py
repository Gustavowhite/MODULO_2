# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 09:41:34 2022

@author: KENDO KAPONI
"""

import pandas as pd
import numpy as np
import scipy import stats as st

# aqui lo primoero que se debe hacer es importa el archivo plano o cvs

my_datas = pd.read_csv('student_data.cvs')

the_media_of_edades = np.mean(my_datas["age"])
the_median_of_edades = np.median(my_datas["age"])
the_desvia_stand_edads = np.std(my_datas["age"])
the_varian_of_edades = np.var(my_datas["age"])

print("la media de las edades es: {}".format(str(the_media_of_edades)))
print("la madiana de las edades es: {}".format(str(the_median_of_edades))
print()
      
