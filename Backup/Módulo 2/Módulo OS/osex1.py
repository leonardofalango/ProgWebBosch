# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 08:14:08 2022

@author: Leonardo Falango
"""

import os

#os.chdir("c:/Users/disrct/Desktop")
novo_local = os.path.join('Nova pasta', 'coala.jpg')
os.rename('coala.jpg', novo_local)
