# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:07:05 2022

@author: DISRCT
"""

import os

def ext(arquivo):
    ext = arquivo.split('.')
    extencao = ext[len(ext) - 1]
    return extencao





def organizar(diretorio):
    audio = os.path.join(diretorio, 'Áudios')
    img = os.path.join(diretorio,'Imagens')
    vid = os.path.join(diretorio,'Vídeos')
    doc = os.path.join(diretorio,'Documentos')
    outros = os.path.join(diretorio, 'Outros')
    
    if not os.path.isdir(audio):
        os.mkdir(audio)
    if not os.path.isdir(img):
        os.mkdir(img)
    if not os.path.isdir(vid):
        os.mkdir(vid)
    if not os.path.isdir(doc):
        os.mkdir(doc)
    if not os.path.isdir(outros):
        os.mkdir(outros)

    lista = os.listdir(diretorio)
    
    eaudio = ['mp3', 'wav']
    eimg = ['png', 'jpeg', 'jpg']
    evid = ['mp4', 'mov', 'avi']
    edoc = ['txt', 'docx', 'pdf','log']
    
    pasta = ''
    for arquivo in lista:
        if os.path.isfile(os.path.join(diretorio, arquivo)) == True:
            extencao = str.lower(ext(arquivo))
            if extencao in eaudio:
                pasta = audio
            elif extencao in eimg:
                pasta = img
            elif extencao in evid:
                pasta = vid
            elif extencao in edoc:
                pasta = doc
            else:
                pasta = outros
        
            os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio,pasta,arquivo))
            print(f'O arquivo {arquivo} do tipo {extencao}, foi movido de {os.path.join(diretorio, arquivo)} para {os.path.join(diretorio,pasta,arquivo)}')
                    
            

organizar("S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Módulo 2/Módulo OS/Organizar")












#
#S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/10 - Aprendizes/6 - Programador Web 2022/Leonardo Falango/Módulo 2/Módulo OS/