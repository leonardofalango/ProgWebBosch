# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:12:22 2022

@author: Leonardo Falango
"""

'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- PROVA -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''

import numpy as np


# 1) criar array 7x7 números aleatórios, 8 > número > 3, numero = -1

array = np.random.randint(0,10, size=49)
array = np.resize(array,(7,7))
print(f'Array Original:\n{array}')

condicao = (array>3) & (array<8)
array[condicao] = -1
print(f'\n\nArray com a condição:\n{array}')
