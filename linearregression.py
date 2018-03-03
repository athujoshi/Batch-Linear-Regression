#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:03:28 2018

@author: atharvajoshi
"""

import numpy as np

x=np.transpose(np.array([[1,2,3,4,5,6,7,8,9]]))
y=np.transpose(np.array([[2,4,6,8,10,12,14,16,18]]))
w=np.random.rand(1,1)

for p in range(100):
    k=(y-(x.dot(w)))
    l=(np.transpose(x)).dot(k)
    c=np.sum(l)
    w=w+(0.001*c)
    