# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 07:27:16 2022

@author: KENDO KAPONI
"""


import numpy

import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

#plt.xlabel('edad')
#plt.ylabel('velocidad')
#plt.title('distribucion de los datos aleatorios')

