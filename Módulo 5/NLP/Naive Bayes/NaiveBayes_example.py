# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:03:29 2022

@author: Leonardo Falango
"""
# Importing
import pandas as pd
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from nltk.metrics import ConfusionMatrix

# Reading DataBase
complete_data = pd.read_table("S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Módulo 5/NLP/spam.csv", encoding='latin-1', sep=';')
# print(complete_data.head())

complete_data = complete_data[['SMS_Text', 'Class']]
# print(complete_data.head())



data = list(complete_data.itertuples(index=False, name=None)) # Converting to list for NLTK

# Training
train, test = train_test_split(data, test_size=0.25)


# Defining functions

# def aply_stem(data):
#     import nltk
#     stopwords = nltk.corpus.stopwords.words("english")
#     snowball_stemmer = SnowballStemmer("english")
#     frasesstemming = []
    
#     for (word, classification) in data:
#         comstemming = [str(snowball_stemmer.stem(p)) for p in nltk.word_tokenize(word) if p not in stopwords and p.isalpha()]
#         frasesstemming.append((comstemming, classification))
        
def aply_stem(data):
    import sys
    sys.path.insert(0, '../NLTK')
    from NLTK_examples_tokenization import clean
    from NLTK_examples_stemming_lemming import stemming
    
    stemming_phrases = []
    for (w, clas) in data:
        try:
            w = clean(w)
            w = stemming(w)
            stemming_phrases.append(w)
        except TypeError:
            continue
    return stemming_phrases

print(aply_stem(data))