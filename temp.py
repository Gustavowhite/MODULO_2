# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# CODE
import pandas as pd

my_data = {
    
            "student": ['jimena', 'juan pablo', 'santiago'],
            "age": [19, 20, 20],
            "sex": ['female', 'male', 'male']
            
    }

df = pd.DataFrame(my_data)
df

print(df['age'])

print(df['student'])

print(df['sex'])

