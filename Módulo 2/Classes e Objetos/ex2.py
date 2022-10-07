# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 08:40:25 2022

@author: Leonardo Falango
"""


class Carro():
    cars = 0
    precos = []
    def __init__(self, modelo, preço, ano = 2021,cor='Prata'):
        self.modelo = modelo
        self.ano = ano
        self.preço = preço
        self.cor = cor
        self.teto = 'Fibra de Carbono'
        self.estadoPortas = 'Fechado'
        Carro.cars += 1
        Carro.precos.append(preço)
    
    def abrirPortas(self):
        print('Abrindo Portas')
        self.estadoPortas = 'Aberto'
    
    def fecharPortas(self):
        print('Fechando Portas')
        self.estadoPortas = 'Fechado'
        
    def acelerar(self):
        print(f"Acelerando o {self.modelo}\nVruuuuuuuuuuuuuuuuuuuuuuuuuuuum")
    
    @staticmethod
    def quantidadeCarros():
        quantCarros = Carro.cars
        precoTotal = sum(Carro.precos)
        print(f'Quantidade de carros no estacionamento {quantCarros}\nValor total dos carros: {precoTotal}')
        
        
    def show(self):
        print(f"\nCarro: {self.modelo}\nPreço: R${self.preço},00\nAno: {self.ano}\nCor: {self.cor}\n")
    
    

ferrari = Carro('Ferrari 157',  596000, 2020,'Vermelha')
fusca = Carro('Fusquinha', 7000, 2005, 'Azul')
porshe = Carro('Porshe Panamera', 350000)

ferrari.show()
fusca.show()
porshe.show()

print(f'\nEstado das portas da Ferrari: {ferrari.estadoPortas}')
ferrari.abrirPortas()
print(f'Estado das portas da Ferrari: {ferrari.estadoPortas}\n')

ferrari.acelerar()
fusca.acelerar()

print('\nCarro: {} Teto: {}\nCarro: {} Teto: {}\nCarro: {} Teto: {}'.format(ferrari.modelo,ferrari.teto,fusca.modelo,fusca.teto, porshe.modelo, porshe.teto))
print('Usando o método estático para mostrar a quantidade de carros no estacionamento')
Carro.quantidadeCarros()

        
        











