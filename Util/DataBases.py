# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:27:13 2022

@author: Leonardo Falango
"""
import pandas as pd
def DataBaseNomes(quantNomes):
    # import pandas as pd
    import random
    df = pd.read_csv("S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Util/nomesobrenome.csv", sep=";", encoding='latin-1')
    
    nomes = []
    while len(nomes) < quantNomes:
        nome = df["nome"].loc[random.randint(0, len(df) - 1)]
        nome = str(nome) + " " +str(df["sobrenome"].loc[random.randint(0, 881)])
        nomes.append(nome)
    return nomes


def mklist():
    mklist = []
    inp = input("Insert data: ")
    while inp != "":
        mklist.append(inp)
        inp = input("Insert data: ")
    return mklist


def sublist(str1, str2, vector):
    for i in range(len(vector)):
        if(str(str1) == vector[i]):
            vector[i] = str(str2)
    return vector


# db = DataBaseNomes(80000)
# csv = {"Nome Completo" : db}
# csv = pd.DataFrame(csv)
# csv.to_csv("NomesCompletosTeste.csv")