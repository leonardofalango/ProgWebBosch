# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 09:42:25 2022

@author: Leonardo Falango
"""

# pi = 1 - 1/3 + 1/5 + 1/7.....

def pi(aprox):
    pi = 0
    k= 1
    for i in range(2,aprox*2,1):
        if i % 2 == 0:
            pi += 4/k
        else:
            pi -= 4/k
        k+=2
    return pi

while True:
    x = int(input())
    print(pi(x))