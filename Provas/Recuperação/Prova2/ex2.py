# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:15:29 2022

@author: Leonardo Falango
"""

import pandas as pd

# 2) Porcentagem de passageiros homens e mulheres no titanic

df = pd.read_csv('Dados/titanic.csv', usecols=['sex'])

male = df[df['sex'] == 'male']
female = df[df['sex'] == 'female']

pct_male = len(male.count(1))
pct_female = len(female.count(1))
pct_total = pct_male + pct_female
# Regra de 3
#100% --- pct_total
#x% --- pct_male/pct_female
pct_male = 100*pct_male / pct_total
pct_female = 100*pct_female / pct_total

print(f"Homens no titanic: {pct_male}%\nMulheres no titanic: {pct_female}%")

