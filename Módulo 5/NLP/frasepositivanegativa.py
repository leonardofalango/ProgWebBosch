# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:23:26 2020

@author: OLV2CT
"""

import pandas as pd
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from nltk.metrics import ConfusionMatrix
import nltk
#Definindo as funções

#Tkeniza as palavras e aplica stemming

def aply_stem(data):
    stopword = nltk.corpus.stopwords.words("english")
    snowball_stemmer=SnowballStemmer("english")
    frasesstemmin=[]
    for (words,classification) in data:
        comstemming=[str(snowball_stemmer.stem(p)) for p in nltk.word_tokenize(words) if p not in stopword and p.isalpha()]
        frasesstemmin.append((comstemming, classification))
    return frasesstemmin


#Extrair todas as palavras
def search_words(setences):
    bag_words=[]
    for (words, classification) in setences:
        bag_words.extend(words)
    return bag_words


#Verificar a frequência das palavras
def verify_freq(words):
    words=FreqDist(words)
    return words

#Salvar as palavras únicas
def search_unique_words(freq):
    freq_unique_words=freq.keys()
    return freq_unique_words

#Função utilizada no classificador para extrair
#as palavras únicas da entrada
def extract_words(document):
    doc=set(document)
    features={}
    for words in unique_words:
        features['%s' % words] =words in doc # %s é a máscara para dizer que sempre a entrada será do tipo string
    return features
        




# Carregando os dados
complete_data = pd.read_csv("S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Módulo 5/Corona_NLP.csv",  encoding = 'latin-1')
# Selecionado as colunas
complete_data = complete_data[['OriginalTweet', 'Sentiment']]
# Convertendo em lista
# Entrada para o nltk
complete_data = list(complete_data.itertuples(index=False,name=None))
# Separando as bases
data_train, data_test = train_test_split(complete_data, test_size=0.20)

################### Train ######################
# Tokenização e stemização
stem_train = aply_stem(data_train)
print(stem_train[0])
# Separando as palavras
words_train = search_words(stem_train)
# Verificando as frequências
freq_words_train = verify_freq(words_train)
print(freq_words_train.most_common(10))
# Separando as palavras únicas
unique_words = search_unique_words(freq_words_train)
# Gerando a tabela com as features
naive_bayes_train = nltk.classify.apply_features(extract_words, stem_train)
############ Classifier ############
nb_classifier = nltk.NaiveBayesClassifier.train(naive_bayes_train)
print(nb_classifier.labels())
print(nb_classifier.show_most_informative_features(10))
########## Data Test ###########
stem_test = aply_stem(data_test)
words_test = search_words(stem_test)
freq_test = verify_freq(words_test)
unique_words_test = search_unique_words(freq_test)
naive_bayes_test = nltk.classify.apply_features(extract_words, stem_test)
######### Verify Accuracy ###########
print(nltk.classify.accuracy(nb_classifier, naive_bayes_train))
print(nltk.classify.accuracy(nb_classifier, naive_bayes_test))
esperado = []
previsto = []

for (frase, sentimento) in naive_bayes_test:
    result = nb_classifier.classify(frase)
    esperado.append(sentimento)
    previsto.append(result)
    
confusion_matrix = ConfusionMatrix(esperado, previsto)
print(confusion_matrix)
sentence = [('My friend died last night', 'None'),
            ('I love you', 'None'),
            ('I have hunger', 'None')]

sentence_stem = aply_stem(sentence)
words_sentence = search_words(sentence_stem)
freq_sentence = verify_freq(words_sentence)
unique_words_sentence = search_unique_words(freq_sentence)
print('-'*50)
frase = nltk.classify.apply_features(extract_words, sentence_stem)
print(frase)
for (f, s) in frase:
    print(nb_classifier.classify(f))
    print("Pronto!")