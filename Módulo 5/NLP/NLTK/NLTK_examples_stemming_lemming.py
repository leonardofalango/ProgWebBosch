# # -*- coding: utf-8 -*-
# """
# Created on Mon May  9 10:30:15 2022

# @author: Leonardo Falango
# """
# # This file is a continuation of NLP
# # The first file is "NTLK_examples_tokenization.py" has to be import
# from NLTK_examples_tokenization import getText, getWords, getWordsNoPunc, getAllWords

# # Printing separator
# def sep():
#     print("_"*50)




# # =============================================================================
# # Stemming
# # =============================================================================

# # Importing stemming alg
# from nltk.stem import SnowballStemmer



# # Specifing language
# sb_stemmer = SnowballStemmer("english")

# words_stemming = []

# clean_words = getWords()
# for w in clean_words:
#     word = sb_stemmer.stem(w)
#     words_stemming.append(word)
# print("->"*5,"Stemming" ,"<-"*5)
# sep()
# print(f"Tamanho: {len(words_stemming)}")
# print(f"Todas as stemming words:\n{words_stemming}")



# # Setting words
# words_stemming = list(set(words_stemming))
# print("\n\nTamanho atual: {}".format(len(words_stemming)))
# print("Palavras atuais:\n{}".format(words_stemming))
# sep()



# # =============================================================================
# # Lemming
# # =============================================================================

# # Importing lemming  alg
# from nltk.stem import WordNetLemmatizer

# lemmatizer = WordNetLemmatizer()
# words_lemma = []

# clean_words = getWords()
# # Applying lemmatization
# for w in clean_words:
#     word = lemmatizer.lemmatize(w)
#     words_lemma.append(word)

# print("->"*5,"Lemming" ,"<-"*5)
# # Setting words
# words_lemma = list(set(words_lemma))
# print(f"\n\nTamanho: {len(words_lemma)}")
# print(f"Palavras atuais:\n{words_lemma}")

# # =============================================================================
# # Comparing both algs
# # =============================================================================
# sep()
# print("\n\nComparação:")
# for i in range(len(words_lemma)):
#     try:    
#         print(f"{words_stemming[i]} | {words_lemma[i]}")
#     except IndexError:
#         continue



# Stemming is faster than Lemming, but Lemming is more precise than Stemming
# Both algorithm can be used NLP
# Methods for import
def stemming(clean_data):
    from nltk.stem import SnowballStemmer
    # Specifing language
    sb_stemmer = SnowballStemmer("english")
    
    words_stemming = []
    
    for w in clean_data:
        word = sb_stemmer.stem(w)
        words_stemming.append(word)

    words_stemming = list(set(words_stemming))
    
    
def lemming(clean_data):
    from nltk.stem import WordNetLemmatizer  
    lemmatizer = WordNetLemmatizer()
    words_lemma = []
    for w in clean_data:
        word = lemmatizer.lemmatize(w)
        words_lemma.append(word)
    
    words_lemma = list(set(words_lemma))
    return words_lemma

    