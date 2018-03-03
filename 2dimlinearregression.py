#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:18:29 2018

@author: atharvajoshi
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv('1.csv')
x = dataset.iloc[:,[3,4]].values
y = dataset.iloc[:, [5]].values
np.shape(y)

w=np.random.rand(2,1)

for p in range(500):
    k=(x.dot(w))
    k=y-k
    print (k)
    x_1=(x)[:,[0]]
    x_2=(x)[:,[1]]
    l_1=np.transpose(x_1).dot(k)
    l_2=np.transpose(x_2).dot(k)
    c_1=0.00001*np.sum(l_1)
    c_2=0.00001*np.sum(l_2)
    v=np.transpose(np.array([[c_1,c_2]]))
    w=w+v
    