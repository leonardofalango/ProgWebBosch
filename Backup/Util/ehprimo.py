# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:39:14 2022

@author: Leonardo Falango
"""

def ehprimo(x):
    if x <= 0:
        return 0
    if x == 1:
        return 0
    if x == 2:
        return 1
    div = 0
    for i in range(x):
        if div >= 2:
            return 0
        if x % (i+1) == 0:
            div +=1
    if div == 2:
        return 1



