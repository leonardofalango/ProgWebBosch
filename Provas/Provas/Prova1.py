# -*- coding: utf-8 -*-

#Created on Tue Feb  1 08:02:51 2022

#@author: Leonardo Falango

'''

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= PROVA =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


'''

  #=================================================== EX 1 ===================================================#

#1) Bhaskara


# def Bhaskara(a, b, c):
#     # x = -b +- (b² - 4 ac / 2) / 2a
#     #Sao três casos: 1 -> delta positivo (2 raízes reias) delta zero (uma raiz real) e delta negativo (nenhuma raíz real)
#     delta = (b**2) - (4*a*c)

#     if delta == 0:
#         x1 = -b / (2*a)
#         x2 = x1
#         print(f"Teremos 1 raiz: {x1}")
#         return x1,x2 #Caso queira fazer contas com x1,x2 retornaremos os numeros, para usa-los 'x,y = Bhaskara(a,b,c)'
#     elif delta > 0:
#         x1 = (-b + (delta**(1/2))) / (2 * a)
#         x2 = (-b - (delta**(1/2))) / (2 * a)
#         print(f"Teremos 2 raizes: {x1} e {x2}")
#         return x1,x2
#     else:
#         print("Não há raízes")
#         return False #Se der Type error, quer dizer que não ha raízes






# try:
#     a = float(input("Entre com o valor de a: "))
#     b = float(input("Entre com o valor de b: "))
#     c = float(input("Entre com o valor de c: "))
    
#     Bhaskara(a, b, c)
# except ValueError:
#     print("ERRO. Entre com valores float.")
# except ZeroDivisionError:
#     print("ERRO. Entre com valores válidos")









  #=================================================== EX 2 ===================================================#
  
  #2) Data completa para abreviada
  
def data(dia,mes,ano):
    print(f"{dia}/{mes}/{ano}")

# Já tinha feito uma lista de meses:
mesesb = []
mesesb.append("Janeiro")
mesesb.append("Fevereiro")
mesesb.append("Março")
mesesb.append("Abril")
mesesb.append("Maio")
mesesb.append("Junho")
mesesb.append("Julho")
mesesb.append("Agosto")
mesesb.append("Setembro")
mesesb.append("Outubro")
mesesb.append("Novembro")
mesesb.append("Dezembro")
# Poderia ter feito uma lista ja pronta 'meses = ["janeiro", "fevereiro", "março" ...]'


stringData = input("Digite a data atual (ex: 14 de Julho de 2020): ")

try:
    dia,mes,ano = stringData.split(" de ") # Separar os dias os meses e os anos
    mes = mes.lower() # Mudando os caracteres do mes todos para minúsculo
    for i in range(len(mesesb)): # Verificar se o mes existe na lista de meses, para que indique se o valor esta colocado corretamente
        mesesb[i] = mesesb[i].lower()
        if mesesb[i] == mes:
            confirmar = True
            break
        else:
            confirmar = False
    dia = int(dia)
    if dia > 31:
        a = int("a") # Vai dar ValueError caindo assim no except, sendo assim, os valores estão inválidos
    ano = int(ano)
    if confirmar:
        stringI = str(i + 1).rjust(2, '0') # Ficar com 2 digitos no mês
        print("{}/{}/{}".format(dia,stringI,ano))
    else:
        a = int("a")

except ValueError:
    print("ERRO. Valores inválidos.")












#     #=================================================== EX 3 ===================================================#
    
#     #3) Desempenho do jogador de futebol
    

# jogadores = {}
# p = 1
# while True:
#     nome = "Jogador " + str(p)
#     gols = []
#     jogador = input("Digite o nome do jogador: ")
#     if jogador == "": #Condição de parada eh colocar uma empty string no nome do jogador
#         break
#     try:
        
#         quantPartidas = int(input("Digite a quantidade de partidas jogadas: "))
        
#         if quantPartidas < 0 :
#             a = int("a") # Forçar um erro caso a quantidade de pertidas jogadas seja menor que 0
            
            
#         for i in range(quantPartidas):
#             quantGols = int(input(f"Quantos gols na partida {i}? "))
            
#             if quantGols < 0:
#                 gols.append(0)
#                 continue
                
#             gols.append(quantGols)
            
#     except ValueError:
#         print("ERRO. Valor inválido")
#         continue
    
#     auxiliar = {"Nome" : jogador, "Gols" : gols, "Total" : sum(gols), "Partidas" : quantPartidas}
#     jogadores[nome] = auxiliar
#     p+=1
    
# print(jogadores)

# for i in range(len(jogadores)):
#     i += 1
#     ident = "Jogador "+ str(i)
#     print("\nO jogador",jogadores[ident]["Nome"],"jogou",jogadores[ident]["Partidas"],"partidas")
#     for j in range(jogadores[ident]["Partidas"]):
#         print(f"Na partida {j} fez {jogadores[ident]['Gols'][j]}")
#     print(f"Com um total de {jogadores[ident]['Total']} gols\n")



















#   #=================================================== EX 4 ===================================================#
 
  #4) Separação de divisões
  
times = ["1_palmeiras", "2_coritiba", "1_corinthians" , "3_juventude", "2_fluminese", "3_bahia", "1_cuiaba",
          "2_cascavel", "3_ponte preta", "2_parana clube", "3_voltaredonda"]

print(times)

div1 = []
div2 = []
div3 = []

for i in range(len(times)): # Percorrer a lista toda
    divisao, time = times[i].split("_") # Separar a divisao '1', '2' ou '3' e separar os times
    divisao = int(divisao)
    if divisao == 1: # Se a divisao for 1, adiciona o time nela e assim por diante
        div1.append(time)
    elif divisao == 2:
        div2.append(time)
    else:
        div3.append(time)
            
print(f"Primeira divisão: {div1}")
print(f"Segunda divisão: {div2}")
print(f"Terceira divisão: {div3}")














#     #=================================================== EX 5 ===================================================#
    
#     #5) Joquempô
    
    
# import random as rd


# def ganhou():
#     global scorePlayer, scoreMaquina
#     print("Você ganhou!")
#     scorePlayer += 1
#     if confirmar() == 0:
#         print(f"Seu score: {scorePlayer}")
#         print(f"Score maquina: {scoreMaquina}")
#     else:
#         joquempo()
    
    

# def perdeu():
#     global scorePlayer, scoreMaquina
#     print("Você perdeu!")
#     scoreMaquina += 1
#     if confirmar() == 0:
#         print(f"Seu score: {scorePlayer}")
#         print(f"Score maquina: {scoreMaquina}")
#     else:
#         joquempo()


# def confirmar():
#     global scorePlayer, scoreMaquina
#     try:
#         continuar = int(input("Digite 1 para continuar jogando ou 0 para parar\n"))
#         if continuar == 0:
#             return 0
#         elif continuar == 1:
#             return 1
#         else:
#             print("Opção inválida")
#             confirmar()
            
#     except ValueError:
#         print("Digite apenas números.")
#         confirmar()
        




# def joquempo():
#     global scorePlayer,scoreMaquina
#     opcoes = ["pedra", "papel", "tesoura"]
#     try: 
#         jogador = int(input("Escolha sua jogada:\n1 - pedra\n2 - papel\n3 - tesoura\n"))
#         if jogador == 1 or jogador == 2 or jogador == 3:
#             pass
#         else:
#             print("Opção inválida.")
#             joquempo()
            
#         maquina = rd.randint(0, 2)
#         print(f"Jogada da maquina: {opcoes[maquina]}")
        
#         maquina = maquina + 1
        
        
        
#         if maquina == 1 and jogador == 1:
#             print("Empate!")
#             if confirmar() == 0:
#                 print(f"Seu score: {scorePlayer}")
#                 print(f"Score maquina: {scoreMaquina}")
#             else:
#                 joquempo()
#         elif maquina == 1 and jogador == 2:
#             ganhou()
    
#         elif maquina == 1 and jogador == 3:
#             perdeu()
        
        
        
#         if maquina == 2 and jogador == 1:
#             perdeu()
#         elif maquina == 2 and jogador == 2:
#             print("Empate!")
#             if confirmar() == 0:
#                 print(f"Seu score: {scorePlayer}")
#                 print(f"Score maquina: {scoreMaquina}")
#             else:
#                 joquempo()
#         elif maquina == 2 and jogador == 3:
#             ganhou()
        
        
        
#         if maquina == 3 and jogador == 1:
#             ganhou()
#         elif maquina == 3 and jogador == 2:
#             perdeu()
#         elif maquina == 3 and jogador == 3:
#             print("Empate!")
#             if confirmar() == 0:
#                 print(f"Seu score: {scorePlayer}")
#                 print(f"Score maquina: {scoreMaquina}")
#             else:
#                 joquempo()
            
     
#     except ValueError:
#         print("Opção inválida.")
#         joquempo()
        
    
# scorePlayer, scoreMaquina = 0,0
# joquempo() # Para iniciar o jogo
 
 
 
 
 
 
 

 
 
 
 
 

 
 
 
 
 

#       #=================================================== EX 6 ===================================================#
      
  #6) Cifra de cesar

import string
letras = list(string.ascii_lowercase) * 2 #Criando uma lista com todas as letras do alfabeto com ind de 0 a 25
                                          #2 Vezes para conseguirmos pegar o ind de cada letra nao decifrada e somar com o codigo de decifracao
try:
      cod = int(input("Qual o número para codificação? "))
      if cod >= 26 or cod <= 0:
          print("Valor invalido.")

      else:
          palavra = input("Insira a palavra a ser codificada: ")
          codificada = ""
          for i in range(len(palavra)):
              letra = palavra[i]
              for j in range(len(letras)):
                  if letra == letras[j]:
                      letracodificada = letras[j+cod]
                      break
              codificada = codificada+letracodificada
          print("Criptografia:", codificada)
    
except ValueError:
    print("Erro. Apenas números")
    













#         #=================================================== EX 7 ===================================================#

# #7
















