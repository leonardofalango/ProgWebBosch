# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:33:42 2022

@author: DISRCT
"""

import fibonacci

try:
    n = int(input("Entre com o número de fatores: "))
    if n <= 0:
        int('a')
    print(fibonacci.fib(n))
except ValueError:
    print("Valor inválido.")