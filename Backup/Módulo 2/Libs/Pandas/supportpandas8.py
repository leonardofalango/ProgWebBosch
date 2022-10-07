# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:16:17 2022

@author: DISRCT
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:39:57 2022

@author: DISRCT
"""


import pandas as pd


vendas = []
quant = []
anos = []

while True:
    venda = float(input('Valor: '))
    if venda == -1:
        break
    quan = float(input('Quantidade: '))
    ano = int(input('Ano'))
    vendas.append(venda)
    quant.append(quan)
    anos.append(ano)
    
    
csv = {'Valor de Venda' : vendas, 'Quantidade de peças' : quant, 'Data da venda' : anos}
df = pd.DataFrame(csv)
df.to_csv('Exercício7.csv', encoding=('utf-8'),index=False)
