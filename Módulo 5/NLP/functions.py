# -*- coding: utf-8 -*-
"""
Created on Tue May 10 09:31:59 2022

@author: Leonardo Falango
"""

def clean(data):
    import nltk
    text_words = nltk.word_tokenize(data)
    text_words_no_punc = []
    for word in text_words:
        if word.isalpha():
            text_words_no_punc.append(word.lower())
    from nltk.corpus import stopwords

    stopwords = stopwords.words("english")
    clean_words = []
    for w in data:
        if w not in stopwords:
            clean_words.append(w)
    return text_words

def stemming(data):
    from nltk.corpus import stopwords
    from nltk.stem import SnowballStemmer
    import nltk
    stopword = stopwords.words("english")
    snowball_stemmer=SnowballStemmer("english")
    frasesstemmin=[]
    for (words,classification) in data:
        comstemming=[str(snowball_stemmer.stem(p)) for p in nltk.word_tokenize(words) if p.lower() not in stopword and p.isalpha()]
        frasesstemmin.append((comstemming, classification))
    return frasesstemmin
    
    
def lemming(clean_data):
    from nltk.stem import WordNetLemmatizer  
    lemmatizer = WordNetLemmatizer()
    words_lemma = []
    for w in clean_data:
        word = lemmatizer.lemmatize(w)
        words_lemma.append(word)
    
    words_lemma = list(set(words_lemma))
    return words_lemma

def search_words(setences):
    bag_words=[]
    for (words, classification) in setences:
        bag_words.extend(words)
    return bag_words

def freq(words):
    from nltk.probability import FreqDist
    words=FreqDist(words)
    return words

def extract_words(document, unique_words):
    doc=set(document)
    features={}
    for words in unique_words:
        features['%s' % words] = words in doc # %s é a máscara para dizer que sempre a entrada será do tipo string
    return features