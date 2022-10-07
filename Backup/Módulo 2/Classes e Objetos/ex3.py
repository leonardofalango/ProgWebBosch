# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:18:10 2022

@author: Leonardo Falango
"""
import time

class Pessoa:
    def __init__(self, nome, cpf, endereco, idade):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.idade = idade
    
    def show(self):
        print(f'\nPessoa: {self.nome}\nCpf: {self.cpf}\nEndereço: {self.endereco}\nIdade: {self.idade}\n')





class Carro:
    # Propriedades
    # dono
    # modelo
    # cor
    # assento, padrao --> 4
    # portas, padrao --> 4
    # velocidade   
    
    
    velocidade = 0
    
    def __init__(self, Pessoa, modelo, cor, velMax,assentos=4,portas=4):
        self.dono = Pessoa
        self.modelo = modelo
        self.cor = cor
        self.assentos = assentos
        self.portas = portas
        self.velMax = velMax
        
    # Métodos
    def acelerar(self, kmh):
        print('Acelerando...')
        for i in range(5):
            print('.')
            time.sleep(0.80)
            
        self.velocidade += kmh
        if self.velocidade >= self.velMax:
            print(f'{self.modelo} está na velocidade max: {self.velMax}km/h')
            self.velocidade = self.velMax
        else:
            print(f'O carro está a: {self.velocidade}km/h')    
    
    def frear(self, kmh):
        print('Freando...')
        for i in range(5):
            print('.')
            time.sleep(0.80)
        
        self.velocidade -= kmh
        if self.velocidade <= 0:
            print(f'{self.modelo} Parado!')
            self.velocidade = 0
        else:
            print(f'{self.modelo} está a: {self.velocidade}km/h') 
        
        
    def verificaDono(self):
        idade = self.dono.idade
        if idade >= 18:
            return True
        else:
            return False
        
        
    def show(self):
        print(f'Dono do carro: {self.dono.nome}\nModelo: {self.modelo}\nCor: {self.cor}\nAssentos: {self.assentos}\nPortas: {self.portas}')
        





leonardo = Pessoa('Leonardo Falas','09093369970','Rua das Torres 198', 18)
jorge = Pessoa('Jorge Silva', '09093364758', 'Rua dos Anjos', 15)

onix = Carro(leonardo, 'onix LTZ', 'Cinza', 203)
caminhao = Carro(jorge, 'Caminhãozão monstro', 'Vermelho', 3,2)

        

leonardo.show()
jorge.show()

onix.show()
print(f'O proprietário do {onix.modelo} pode dirigir: {onix.verificaDono()}')
# onix.acelerar(100)
# onix.acelerar(103)
# onix.frear(400)

# Carro e pessoa funcionando






class Casa:
    def __init__(self, Pessoa,tamanho, comodos, tvs, cor): # tvs sria a quantidade de tvs
        self.proprietario = Pessoa    
        self.tamanho = tamanho
        self.comodos = comodos
        self.tvs = tvs
        self.cor = cor
        self.estadoLuz = []
        for i in range(len(comodos)):    
            self.estadoLuz.append(False) 
    
    def acenderLuz(self, comodo):
        comodo -= 1
        if self.estadoLuz[comodo] == True:
            print(f'Luz do comodo: {self.comodos[comodo]} já esta acesa')
        else:
            print(f'Acendendo a luz do comodo: {self.comodos[comodo]}')
            self.estadoLuz[comodo] = True
            
        
    def apagarLuz(self, comodo):
        comodo -= 1
        if self.estadoLuz[comodo] == False:
            print(f'Luz do comodo: {self.comodos[comodo]} já esta apagada')
        else:
            print(f'Apagando a luz do comodo: {self.comodos[comodo]}')
            self.estadoLuz[comodo] = False
        
    def Casashow(self):
        print(f'Proprietário: {self.proprietario.nome}\nTamanho: {self.tamanho}m²\nComodos: {self.comodos}\nQuantidade de TVS: {self.tvs}\nCor: {self.cor}\n')
        
        
        
comodos_leo = ['Sala','Cozinha','Quarto léo','Quarto Visita']
print('\n\n\n')
casa_leo = Casa(leonardo, 150, comodos_leo, 5, 'Branca')
casa_leo.Casashow()
casa_leo.acenderLuz(1)
casa_leo.apagarLuz(2)
casa_leo.acenderLuz(2)
casa_leo.apagarLuz(2)
print('\n\n\n')

# Casa ja está funcionando





class motorHome(Carro,Casa):
    def __init__(self, Pessoa, modelo, cor, velMax, comodos, portas, tamanho, tvs):
        Carro.__init__(self, Pessoa, modelo, cor, velMax, len(comodos))
        Casa.__init__(self, Pessoa, tamanho, comodos, tvs , cor)
        
        



comodos = ['Volante','Quarto 1', 'Quarto 2']
trailer_leo = motorHome(leonardo, 'Caminhãozão Monstro', 'Branco', 120, comodos, 2, 24, 3)
trailer_leo.Casashow() # Printar os atributos da Casa
trailer_leo.show() # Printar os atributos do Carro
trailer_leo.acelerar(100) # Como o motorhome é um carro, ele tem as funções do carro
trailer_leo.acenderLuz(2) # Como o motorhome também é uma casa, ele também tem as funções da casa
trailer_leo.apagarLuz(2)
trailer_leo.apagarLuz(2)
trailer_leo.frear(100)







