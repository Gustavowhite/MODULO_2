# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:05:07 2022

@author: KENDO KAPONI
"""

# Date of student
# Name: GUSTAVO BLANCO JARAMILLO
# ID: 502603
# gustavoj.blanco@upb.edu.co




# Lo primero que se debe hacer para realizar este ejercicio es una asignacion
# variables con su respectivos valores de la ecuacion...

a = 4
b = 5
c = 6
d = 7
e = 8
f = 9

# aqui se la variable ecua1 recibe el valor de la operacion que esta despues del =
# la ecua2 recibe el valor de la eperacion que esta despues del = y lo guarda mas
# no lo muestra para ambos casos de la ecua1 y ecua2

ecua1 = (a+(b/c))/(d+(e/f))

Ecua2 = a-(b/(c-d))

# aqui se realiza el punto 3 y 4 del taller en el paso de los datos de la variables

Ecua3 = ecua1
ecua1 = Ecua2
Ecua2 = Ecua3

# aqui por ultimo imprimimos los resultados de las operaciones y que es el ultimo 
# punto del ejercio.

print(ecua1)
print(Ecua2)
