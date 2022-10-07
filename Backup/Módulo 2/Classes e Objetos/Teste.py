# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 08:16:03 2022

@author: Leonardo Falango
"""


class Casa:
    def __init__(self, area, rua, cor, proprietario = None):
        self.area = area
        self.rua = rua
        self.cor = cor
        self.proprietario = proprietario
        Casa.energia = True
        
    def printarTudo(self):
        if self.proprietario is None:
            proprietario = 'Alguem'
            
        else:
            proprietario = self.proprietario
            
        print(f'{proprietario} tem uma casa {self.cor} de {self.area}m² na rua {self.rua}. Energia : {Casa.energia}')
   
    @staticmethod
    def cortarEnergia():
        Casa.energia = False
        print('Energia cortada!')
        
    @staticmethod
    def ligarEnergia():
        Casa.energia = True
    
    
casa_joao = Casa(240, 'Vicente Machado', 'Azul', 'João')
casa_leonardo = Casa(1800, 'Rua inventada 138', 'Cinza', 'Leonardo')
casa_joaquim = Casa(120, 'Rua das flores', 'Azul')
casa_joao.printarTudo()
casa_leonardo.printarTudo()
casa_joaquim.printarTudo()

Casa.cortarEnergia()

casa_joaquim.printarTudo()
casa_joao.printarTudo()
casa_leonardo.printarTudo()