# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:17:22 2022

@author: Leonardo Falango
"""

import matplotlib.pyplot as plt
import math
import numpy as np

# 4) subplots com 2 gráficos, 2 linhas 1 coluna, f(x) = sen(x) e g(x) = cos(x)
#eixo x compartilhado utilize a lib math, multiplica x por 2π para fazer em radiano

#def seno(x):
#    return math.sin(x)
#def cos(x):
#    return math.cos(x)
#
#y=[]
#z=[]
#x = np.linspace(-2,2,1000)
#for i in x:
#    y.append(seno(i*(2*math.pi)))
#    z.append(cos(i*(2*math.pi)))
#
#
#fig, eixo = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(12,6))
#
#eixo[0].plot(x,y, color='blue', linewidth = 4, label='Seno de x')
#eixo[1].plot(x,z, color='red', linewidth = 4, label='Cosseno de x')
#eixo[0].grid(True)
#eixo[1].grid(True)
#eixo[1].set_title('Cosseno de x', fontsize=30)
#eixo[0].set_title('Seno de x', fontsize=30)



π = math.pi

def sen(x):
    global π
    x = x * (2 * π)
    return np.sin(x)
def cosseno(x):
    global π
    x = x * (2 * π)
    return np.cos(x)

eixo_x = np.linspace(-2,2,1000)

eixo_y_seno = []
eixo_y_cosseno = []

for x in eixo_x:
    eixo_y_seno.append(sen(x))
    eixo_y_cosseno.append(cosseno(x))


fig, eixo= plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8,6))

eixo[0].plot(eixo_x,eixo_y_seno, color='blue', linewidth = 4, label='Seno de x')
eixo[1].plot(eixo_x,eixo_y_cosseno, color='red', linewidth = 4, label='Cosseno de x')
eixo[0].grid(True)
eixo[1].grid(True)
eixo[1].set_title('Cosseno de x', fontsize=30)
eixo[0].set_title('Seno de x', fontsize=30)
plt.show()



