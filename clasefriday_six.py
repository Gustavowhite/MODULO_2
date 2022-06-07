# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 17:04:48 2022

@author: KENDO KAPONI
"""

import numpy

from scipy import stats

import matplotlib.pyplot as plt

#here it that was is into the date that will be anality

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Mean of speeds

x = numpy.mean(speed)
print(x)

# now, let go for the median

y = numpy.median(speed)
print(y)

# speed - 2

speed_2 = [77, 78, 85, 86, 86, 87, 87, 86, 87, 87, 94, 98, 99, 103]
y_2 = numpy.mean(speed_2)
print(y_2)

# now into at the mode

z = stats.mode(speed)
z2 = stats.mode(speed_2)

print(z)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
print(z2)

#----------------------------------------------------

# ahora vamos para la desviacion estandar "std"

speed_3t = ["v1", "v2", "v3", "v4", "v5", "v6", "v7"]
speed_3 = [86, 87, 88, 86, 87, 85, 86]
std1 = numpy.std(speed_3)
print(std1)

speed_4t = ["v1", "v2", "v3", "v4", "v5", "v6", "v7"]
speed_4 = [32, 111, 138, 28, 59, 77, 97]
std2 = numpy.std(speed_4)
print(std2)
print("plot 1")
plt.bar(speed_3t, speed_3)
print("plot 2")
plt.bar(speed_4t, speed_4)


plt.xlabel('velocidades')
plt.ylabel('km/h')
plt.title('comparacion de velocidad')




