# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:56:47 2020

@author: OLV2CT
"""

import  pandas as pd
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from nltk.metrics import ConfusionMatrix
import nltk

#Lendo a base de dados
complete_data=pd.read_table("spam.csv", encoding='latin-1', sep=";")
print(complete_data.head())
print(complete_data.columns)

#Selecionando as colunas necessárias
complete_data=complete_data[["SMS_Text","Class"]]

#Convertendo em lista
#Entrada para nltk
print(complete_data)
data=list(complete_data.itertuples(index=False, name=None))
print(data)
#Separando os dados que vão ser usados
Train, Test= train_test_split(data, test_size=0.25)
#print(Train)

#Definindo as funções

#Tkeniza as palavras e aplica stemming

def aply_stem(data):
    stopword = stopwords.words("english")
    snowball_stemmer=SnowballStemmer("english")
    frasesstemmin=[]
    for (words,classification) in data:
        comstemming=[str(snowball_stemmer.stem(p)) for p in nltk.word_tokenize(words) if p.lower() not in stopword and p.isalpha()]
        frasesstemmin.append((comstemming, classification))
    return frasesstemmin


#Transformando tudo em tipo string
print(Train)
train_str=[]
for (setence, classs) in Train:
    train_str.append([str(setence),str(classs)])
print(train_str)

#Tokenização e stemização
data_stem=aply_stem(train_str)
print(data_stem)
print(data_stem[1]) 


#Extrair todas as palavras
def search_words(setences):
    bag_words=[]
    for (words, classification) in setences:
        bag_words.extend(words)
    return bag_words


#Seperando as palavras
words_data=search_words(data_stem)
print("w",words_data)

#Verificar a frequência das palavras
def verify_freq(words):
    words=FreqDist(words)
    return words

#Verificando as freq
freq=verify_freq(words_data)
print(freq["u"]) #Freq é um dicionário com a chave palavra e valor frequencia
print(freq.most_common(10))
print(freq.keys())

#Salvar as palavras únicas
def search_unique_words(freq):
    freq_unique_words=freq.keys()
    return freq_unique_words

# Separando as palavras únicas
unique_words = search_unique_words(freq)
print(unique_words)
#Função utilizada no classificador para extrair
#as palavras únicas da entrada
def extract_words(document):
    doc=set(document)
    features={}
    for words in unique_words:
        features['%s' % words] = words in doc # %s é a máscara para dizer que sempre a entrada será do tipo string
    return features
        
# Gerando a tabela com as features
naive_bayes_true_false = nltk.classify.apply_features(extract_words, data_stem)
print(naive_bayes_true_false)
#Criando o classificador
classificador = nltk.NaiveBayesClassifier.train(naive_bayes_true_false)

print(classificador.labels())
print(classificador.show_most_informative_features(10))
test_str = []

for (sentence, classs) in Test:
    test_str.append([str(sentence),str(classs)])
stem_test = aply_stem(test_str)
words_test = search_words(stem_test)
freq_test = verify_freq(words_test)
unique_words_test = search_unique_words(freq_test)
naive_bayes_true_false_test = nltk.classify.apply_features(extract_words, stem_test)

# Verificando acurácia com a base de treinamento
print(nltk.classify.accuracy(classificador, naive_bayes_true_false))
# Verificando acurácia com a base de teste
print(nltk.classify.accuracy(classificador, naive_bayes_true_false_test))
resultado_esperado = []
resultado_previsto = []

for (frase, classe) in naive_bayes_true_false_test:
    resultado = classificador.classify(frase)
    resultado_esperado.append(classe)
    resultado_previsto.append(resultado)
    
matriz_confusao = ConfusionMatrix(resultado_esperado, resultado_previsto)
print(matriz_confusao)

## Testando o classificador
#sentence = [('Your award nokia waits you! Send code 9999 to recieve', 'None')]
#
#sentence_stem = aply_stem(sentence)
#words_sentence = search_words(sentence_stem)
#freq_sentence = verify_freq(words_sentence)
#unique_words_sentence = search_unique_words(freq_sentence)
#
#frase = nltk.classify.apply_features(extract_words, sentence_stem)
#
#for (f, c) in frase:
#    print(classificador.classify(f))
