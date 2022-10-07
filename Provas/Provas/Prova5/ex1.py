# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:46:30 2022

@author: Leonardo Falango
"""

# Imports
import nltk
import pandas as pd
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from nltk.metrics import ConfusionMatrix
from nltk.stem import SnowballStemmer




# Functions

def lemmatize(data):
    stopword = stopwords.words("english")
    snowball_stemmer=SnowballStemmer("english")
    frasesstemmin=[]
    for (words,classification) in data:
        comstemming=[str(snowball_stemmer.stem(p)) for p in nltk.word_tokenize(words) if p.lower() not in stopword and p.isalpha()]
        frasesstemmin.append((comstemming, classification))
    return frasesstemmin


def frequency(sentences):
    words_data = []
    for (words, calssification) in sentences:
        words_data.extend(words)
    freq = FreqDist(words_data)
    return freq.keys()

def search_words(setences):
    bag_words=[]
    for (words, classification) in setences:
        bag_words.extend(words)
    return bag_words

def verify_freq(words):
    words=FreqDist(words)
    return words


def search_unique_words(freq):
    freq_unique_words=freq.keys()
    return freq_unique_words

def extract_words(document):
    doc=set(document)
    features={}
    for words in unique_words:
        features['%s' % words] = words in doc # %s é a máscara para dizer que sempre a entrada será do tipo string
    return features


# Setting database
df = pd.read_csv("Dados/Test.csv")

# Pegando apenas 1500 amostras
df = df.iloc[1:1500, :]

data = list(df.itertuples(index=False, name=None))
# print(data)

# Separando os dados de teste e de treino
Train, Test= train_test_split(data, test_size=0.3, random_state=27)

# Transformando em stings
train_str=[]
for (setence, classs) in Train:
    train_str.append([str(setence),str(classs)])


#Tokenização e stemização
data_stem=lemmatize(train_str)


#Seperando as palavras
words_data=search_words(data_stem)


#Verificar a frequência das palavras
freq=verify_freq(words_data)
print(freq["u"]) #Freq é um dicionário com a chave palavra e valor frequencia
print(freq.most_common(10))
print(freq.keys())


# Salvando as palavras unicas
unique_words = search_unique_words(freq)
print(unique_words)



# Tabela de features
naive_bayes_true_false = nltk.classify.apply_features(extract_words, data_stem)
print(naive_bayes_true_false)


# Instanciando o classificador
classificador = nltk.NaiveBayesClassifier.train(naive_bayes_true_false)

print(classificador.labels())
print(classificador.show_most_informative_features(3))
test_str = []

for (sentence, classs) in Test:
    test_str.append([str(sentence),str(classs)])
stem_test = lemmatize(test_str)
words_test = search_words(stem_test)
freq_test = verify_freq(words_test)
unique_words_test = search_unique_words(freq_test)
naive_bayes_true_false_test = nltk.classify.apply_features(extract_words, stem_test)

resultado_esperado = []
resultado_previsto = []

for (frase, classe) in naive_bayes_true_false_test:
    resultado = classificador.classify(frase)
    resultado_esperado.append(classe)
    resultado_previsto.append(resultado)
    
matriz_confusao = ConfusionMatrix(resultado_esperado, resultado_previsto)
print(matriz_confusao)

# Verificando as acurácias
print("Acurácia Treino: {}".format(nltk.classify.accuracy(classificador, naive_bayes_true_false)))
print("Acurácia Teste: {}".format(nltk.classify.accuracy(classificador, naive_bayes_true_false_test)))


## Testando o classificador
sentence = [('I loved this stand up comedy', 'None'),
            ('I hated this stand up comedy', 'None')]

sentence_stem = lemmatize(sentence)
words_sentence = search_words(sentence_stem)
freq_sentence = verify_freq(words_sentence)
unique_words = search_unique_words(freq_sentence)

frase = nltk.classify.apply_features(extract_words, sentence_stem)
cont = 0
numbers = ['primeira', 'segunda']
for (f, c) in frase:
    print('Classificação para a {} frase: {}'.format(numbers[cont],classificador.classify(f)))
    cont += 1
