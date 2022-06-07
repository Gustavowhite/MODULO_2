# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 21:18:58 2022

@author: KENDO KAPONI
"""

import numpy as np

import matplotlib.pyplot as plt

# generate random values with a uniform distribution

x = np.random.uniform(0.0, 5.0, 250)
print(x)

# histogram

plt.hist(x, 10)
plt.show()