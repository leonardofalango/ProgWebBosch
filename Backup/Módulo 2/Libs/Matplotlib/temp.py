# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:02:36 2022

@author: DISRCT
"""

import matplotlib.pyplot as plt

plt.plot([0,4,8,12,20,37], [0,20,40,60,80,100],label='Ferrari',color='r')
plt.plot([0,8,13,22,37],[0,10,20,40,50], label='Fusquinha', linewidth=2, marker='s',linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Velocidade')
plt.axis([-5,37,0,100])#x,x,y,y
plt.grid(True,linewidth=1,linestyle=':')
plt.show()
