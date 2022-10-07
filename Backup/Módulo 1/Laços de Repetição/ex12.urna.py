# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:33:35 2022

@author: DISRCT
"""

votoMS = 0
votoAR = 0
votoCS = 0
voto = 0
votoNulo = 0
votoBranco = 0
candidatos = ["Maria Santos", "Carlos Silva", "Antônio Rocha", "NULO", "Branco"]


def urna():
    
    global votoMS,votoCS, votoAR, votoNulo, candidatos, voto, votoBranco
    
    
    votos = [votoMS, votoCS, votoAR, votoNulo, votoBranco]
    print("_"*30,"Urna","_"*30)
    try:
        opcao = int(input("1. Candidato Maria Santos \n2. Candidato Carlos Silva \n3. Candidato Antônio Rocha \n4. Nulo \n5. Branco\nEntre com seu voto:"))
        
    except ValueError:
        print("ERRO: Apenas números inteiros são aceitos.")
        urna()
        
    if opcao == 1:
        votoMS += 1
        voto += 1
        urna()
        
    elif opcao == 2:
        votoCS += 1
        voto += 1
        urna()
        
    elif opcao == 3:
        votoAR += 1
        voto += 1
        urna()
        
    elif opcao == 4:
        votoNulo += 1
        voto += 1
        urna()
        
    elif opcao == 5:
        votoBranco += 1
        voto += 1
        urna()
        
    elif opcao == 6:
        
        for i in range(len(candidatos)):
            print(f"\nCandidato: {candidatos[i]}\n Votos: {votos[i]}")
        print("Porcentagem de votos nulos: {:.02f}%".format(votoNulo * 100 / voto))
        print("Porcentagem de votos brancos: {:.02f}%".format(votoBranco * 100 / voto))
        maior = (max(votos))
        ind = votos.index(maior)
        
        
        
        if ind > 2:
            print("Eleição cancelada.")
            urna()
        else:
            vencedor = candidatos[ind]
            print("O candidato vencedor: {}\nCom {:.02f}%!".format(vencedor, (votos[ind] * 100 / voto)))
            urna()
    else:
        print("Valor invalido")
        urna()
 
urna()




