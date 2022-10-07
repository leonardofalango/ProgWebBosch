# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:14:47 2022

@author: Leonardo Falango
"""

import os

def busca(arquivo):
    if os.path.isdir(os.path.join(arquivo)):
        print("O caminho é uma pasta.", os.path.join(arquivo))
    elif os.path.isfile(os.path.join(arquivo)) == True:
        print("O caminho é um arquivo.", os.path.join(arquivo))
    elif os.path.isfile(os.path.join(arquivo)) == False:
        print("O caminho não é um arquivo.", os.path.join(arquivo))
    else:
        print("O caminho não é uma pasta.", os.path.join(arquivo))

busca("cv2.py")