# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 08:39:13 2022

@author: KENDO KAPONI
"""

import numpy

import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

