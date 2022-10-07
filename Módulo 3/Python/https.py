# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:12:07 2022

@author: Leonardo Falango
"""

import requests as req
import json
import cv2
proxie = {'https' : 'https://disrct:saladigital0311@10.224.200.26:8080'}

r = req.get("https://youtube.com/", proxies=proxie)

print("\n\n\n{}".format(r)) ## Se deu reponse 200, quer dizer que funcionou.
## reponse 400, erro no cliente
## reponse 500. erro no servidor

url = 'https://random.dog/woof.json'
img_data = req.get(url, proxies = proxie).content
new_url = json.loads(img_data)['url']

split = new_url.split('.')
ext = split[len(split)-1]

img = req.get(new_url, proxies = proxie)


with open('dog.'+ext, 'wb') as dog_file:
    dog_file.write(img.content)
