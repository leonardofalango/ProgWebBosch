# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 09:13:04 2022

@author: Leonardo Falango
"""


times = ['Coritiba', 'Athletico', 'Paraná']
rodada = []
a = 0
while a == 0:
    try:
        for i in range(3):
            resultado = input(f'Entre com o resultado dsa quatro rodadas do {times[i]}: ex:(V V D E)\n')
            resultado = resultado.upper()
            resultado = resultado.split(" ")
            if len(resultado) != 4:
                int("")
                break
            else:
                vit = resultado.count('V')
                der = resultado.count('D')
                emp = resultado.count('E')
                
                vit = vit*3
                emp = emp*1
                der = der*0
                
                rodada.append(vit+emp+der)
        
        ind = rodada.index(max(rodada))
        print(f"O Time que somou mais pontos foi: {times[ind]}")
        ind = rodada.index(min(rodada))
        print(f"O Time que somou menos pontos foi: {times[ind]}") 
        a = 1
    except ValueError:
        print("ERRO. Entre apenas com valores válidos. ex: (E D V V)")
        
        