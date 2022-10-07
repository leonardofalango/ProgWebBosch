# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:03:34 2022

@author: Leonardo Falango
"""

import time
import json


dias = {"Mon" : "Segunda-feira", "Sun": "Domingo", "Tue": "Terça-feira",
        "Thur":"Quinta-feira", "Fri" : "Sexta-feira", "Sat" : "Sábado"}


time = time.ctime()
dia, mes, descartar, ndia, hora, ano = time.split(" ")
json1 = {hora : dias[dia]}
json = json.dumps(json1)
print(json)