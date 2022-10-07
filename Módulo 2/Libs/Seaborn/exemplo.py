 # -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 08:32:58 2022

@author: DISRCT
"""

import pandas as pd
import seaborn as sns

dataframe = pd.read_csv("seaborn.csv", sep=";")

dataframe.head()


#sns.relplot(x="total_bill", y="tip", hue='day', data=dataframe)
#
#sns.relplot(x="total_bill", y="tip", style='smoker', data=dataframe)
#
## hue altera as cores das bolinhas conforme a legenda, o style altera a bolinha conforme a legenda

#sns.relplot(x="total_bill", y="tip", size='servings', data=dataframe)

## size altera o tamanho da bolinha conforme a quantidade, nesse caso de 'servings'

##EXERCÍCIO 5.1

sns.set_style('darkgrid')

sns.relplot(x="total_bill", y="tip", hue='smoker', style='smoker', data=dataframe)

sns.relplot(x="total_bill", y="tip", hue='servings', palette='Purples', size='servings', data=dataframe)

