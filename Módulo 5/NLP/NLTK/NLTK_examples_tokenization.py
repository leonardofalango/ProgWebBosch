# # -*- coding: utf-8 -*-
# """
# Created on Mon May  9 09:23:55 2022

# @author: Leonardo Falango
# """


# import nltk
# from nltk.probability import FreqDist

# # Abrindo um arquivo de texto
# text_file = open("S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Módulo 5/NLP/Artificial_Intelligence.txt")

# # Lendo o texto do arquivo
# # e atribuindo a uma variavel
# text = text_file.read()
# # print(text)

# # print("=-=-=-=-=-=-=-=-==-=-=-=-=")
# # print("Quantidade de frases: {}".format(len(nltk.sent_tokenize(text))))


# text_words = nltk.word_tokenize(text)
# # print("Quantidade de palavras: {}".format(len(text_words)))

# #Palavras mais comuns
# words_freq = FreqDist(text_words)
# # print(words_freq.most_common(10))

# #Plottando o gráfico das palavras mais comuns
# # words_freq.plot(10)



# # Remoção de pontuação e caracteres especiais
# text_words_no_punc = []

# for w in text_words:
#     if w.isalpha():
#         text_words_no_punc.append(w.lower())

# # print("Quantidade de palavras antes da remoção: {}".format(len(text_words)))
# # print("Quantidade de palavras depois da remoção: {}".format(len(text_words_no_punc)))
# # print("\n\nPalavras sem caracteres especiais, pontuação, etc\n{}".format(text_words_no_punc))
# words_no_punc_freq = FreqDist(text_words_no_punc)
# # print("\n\nAs 10 palavras mais comum no texto: ")
# # print(words_no_punc_freq.most_common(10))

# # Palavras mais comuns
# words_no_punc_freq.most_common(10)

# # Plottando o gráfico das palavras sem acentuação/pontuação mais comuns
# # words_no_punc_freq.plot(10)


# # StopWords palavras que nao influenciam em nada
# from nltk.corpus import stopwords

# stopwords = stopwords.words("english")
# # print(stopwords)


# # Tirando as StopWords do nosso texto
# clean_words = []
# for w in text_words_no_punc:
#     if w not in stopwords:
#         clean_words.append(w)

# # Comparand0o antes e depois da remoção de stopwords
# # print("\n\n____________________________________________________________\nQuantidade de palavras antes: {}\nQuantidade de palavras depois: {}\nPalavras após remoção:\n{}".format(len(text_words_no_punc), len(clean_words), clean_words))





# # Métodos para retornos

# def getText():
#     return text
# def getWords():
#     return clean_words
# def getWordsNoPunc():
#     return text_words_no_punc
# def getAllWords():
#     return text_words

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
