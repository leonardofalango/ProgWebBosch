# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:08:35 2022

@author: DISRCT
"""

import pandas as pd


# s = pd.Series([3,-5,7,9])
# print(s)



# # Pandas trabalha com Dataframas e Series
# dados = {'Nomes' : ['Leonardo', 'Leonardão', 'Leonardinho'],
#          'Área' : ['TI', 'Tecnologia da Informação', 'Tecnologica']}

# data_frame = pd.DataFrame(dados)
# print('\n'*5,data_frame)



# CSV
data_frame = pd.read_csv('teste.csv', index_col=['movieId'], usecols=['genres','movieId']) # O usecols serve para descartas as colunas que você nao quer
print(data_frame)
print(data_frame.describe())
print(data_frame.loc[[1,2,3]]) # Para localizar, com o Id




data_frame = pd.read_csv('teste.csv', index_col=['genres','title']) # INDEX COL PARA ORGANIZAR COM GENEROS PRIMEIRO E TITULO POR SEGUNDO
print(data_frame.loc[['Comedy', 'Drama', 'Comedy|Drama']]) # Para localizar com o Genero

# Colocando condições
print(data_frame.loc[data_frame['movieId'] <= 100])



