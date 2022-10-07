# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:09:49 2022

@author: Leonardo Falango
"""

class Calculadora:
    def __init__(self):
        pass
    
    def soma(self,x,y):
        return x+y
    
    def sub(self,x,y):
        return x-y
    
    def mult(self,x,y):
        return x*y
    
    def div(self,x,y):
        return x/y
    
class CalculadoraCientifica(Calculadora):
    def __init__(self):
        super().__init__()
        
    
    def fatorial(self,x):
        lista = []
        fatorial = 1
        fat = x
        while fat >= 1:
            lista.append(fat)
            fat -= 1
        for i in range(len(lista)):
            numero = lista[i]
            fatorial = fatorial * numero
        return fatorial
    
    def Bhaskara(self,a, b, c):
        # x = -b +- (b² - 4 ac / 2) / 2a
        #Sao três casos: 1 -> delta positivo (2 raízes reias) delta zero (uma raiz real) e delta negativo (nenhuma raíz real)
        delta = (b**2) - (4*a*c)
    
        if delta == 0:
            x1 = -b / (2*a)
            x2 = x1
            print(f"Teremos 1 raiz: {x1}")
            return x1,x2 #Caso queira fazer contas com x1,x2 retornaremos os numeros, para usa-los 'x,y = Bhaskara(a,b,c)'
        elif delta > 0:
            x1 = (-b + (delta**(1/2))) / (2 * a)
            x2 = (-b - (delta**(1/2))) / (2 * a)
            print(f"Teremos 2 raizes: {x1} e {x2}")
            return x1,x2
        else:
            print("Não há raízes")
            return False #Se der Type error, quer dizer que não ha raízes

    
    
calc = CalculadoraCientifica()
print('A = 1 B = -3 e C= 2:')
calc.Bhaskara(1,-3, 2)
print('5! = ',calc.fatorial(5))
print('2 * 3 =',calc.mult(2, 3))
# Mostrando que funcionam as funções da calculadora normal, e tambem da calculadora Científica



