# -*- coding: utf-8 -*-
"""
Created on Tue May 10 09:13:37 2022

@author: Leonardo Falango
"""

# Importing libs
import  pandas as pd
import nltk
from nltk.metrics import ConfusionMatrix
from sklearn.model_selection import train_test_split

# Importing functions from another .py file
from functions import stemming, search_words, freq
# Stemming function returns you the data after stemming
# Lemming function returns you the data after lemming
# Clear function returns you a clean data


# Reading DataBase
path = 'S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Módulo 5/Corona_NLP.csv'
complete_data=pd.read_table(path, sep=',')


# Dropping unnecessary data
complete_data = complete_data[['OriginalTweet', 'Sentiment']]

# Converting to list
complete_data = list(complete_data.itertuples(index=False, name=None))

# Slicing data for training and testing
train_data, test_data = train_test_split(complete_data, test_size=0.30) # Try another values in test_size for better results



train_str = []
for (sentence, clas) in train_data:
    train_str.append([str(sentence), str(clas)])

# Stemming also does tokenization, so you dont have to do before aply stem
data_stem = stemming(train_str)

# Extracting words
all_words = search_words(data_stem)

# Verifying words frequency
words_freq = freq(all_words)
# Frequency is a dict. Key is word and Value is frequency in quantities

# Verifying unique words
unique_words = words_freq.keys()
def extract_words(document):
    doc=set(document)
    features={}
    for words in unique_words:
        features['%s' % words] = words in doc # %s é a máscara para dizer que sempre a entrada será do tipo string
    return features

# Generating features table
naive_bayes_true_false = nltk.classify.apply_features(extract_words, data_stem)
naive_bayes_true_false_test = nltk.classify.apply_features(extract_words, data_stem)

# Generating classificator
classificador = nltk.NaiveBayesClassifier.train(naive_bayes_true_false)

test_str = []
for (sentence, clas) in test_data:
    test_str.append([str(sentence),str(clas)])
stem_test = stemming(test_str)
words_test = search_words(stem_test)
freq_test = freq(words_test)
unique_words_test = freq_test.keys()
naive_bayes_true_false_test = nltk.classify.apply_features(extract_words, stem_test)


# Accuracy in training
print(nltk.classify.accuracy(classificador, naive_bayes_true_false))
# Accuracy in test
print(nltk.classify.accuracy(classificador, naive_bayes_true_false_test))


# Verifying results
real_result = []
pred_result = []

for (sentece, clas) in naive_bayes_true_false_test:
    result = classificador.classify(sentence)
    real_result.append(clas)
    pred_result.append(result)
    
cm = ConfusionMatrix(real_result, pred_result)

print(cm)



## Testing the classificator
sentence = [('Your award nokia waits you! Send code 9999 to recieve', 'None'),
            ('I love you', 'None'),
            ('I have hunger', 'None')]

sentence_stem = stemming(sentence)
words_sentence = search_words(sentence_stem)
freq_sentence = freq(words_sentence)
unique_words_sentence = freq_sentence.keys()

frase = nltk.classify.apply_features(extract_words, sentence_stem)

for (f, c) in frase:
    print(classificador.classify(f))

