# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 08:57:25 2022

@author: KENDO KAPONI
"""

import numpy

import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()