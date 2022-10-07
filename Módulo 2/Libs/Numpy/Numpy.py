# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 08:12:11 2022

@author: DISRCT
"""

import numpy as np


lista = [1,2,3,4,5,6,7,8,9]
array = np.array(lista)
print(array)

# Funcao arange
array = np.arange(1,10)
print(array)


# Funcao reshape
array = np.arange(10).reshape(2,5)
print(array)

array = np.arange(10).reshape(5,2)
print(array)






# Contas com as arrays
print('\n'*10)
array = np.arange(10)
print(array)
# São diferentes da lista
array = array*2
print(array)

lista = [1,2,3,4,5,6,7,8,9]
lista = lista*2
print(lista) # '1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9', ele nao multiplica cada elemento
print('\n'*10)





# Exercício: Crie uma matriz booleana numpy 3x3 com 'True'
'''
matrix = bool(np.zeros(9).reshape(3,3)) # Primeira solução que eu pensei
print(matrix)
# Fazer uma matrix inteira de um numero, e altera-lo para True
for i in range(len(matrix)):
    matrix[i] = True
print(matrix)
# Não deu pois a matrix criada é de float, nao de boolean
'''
matrix = np.full((3,3), True) # Depois de pesquisar, existe uma função que cria arrays cheias do valor que você escolheu
print(matrix)




# Index de arrays inteiros
a = np.array([[1,2],[3,4],[5,6]])
print(a[[0,1,2],[0,1,0]])
print(np.array([a[0,0],a[1,1],a[2,0]])) # ESSA FORMA SÓ FUNCIONA COM ARRAYS










print('\n'*5)
# Exercício: Números ímpares
# Identifique todos os números impares de um array 'arr'

arr = np.array([3,1,2,7,8,9,6,4,3]).reshape(3,3)
print(arr)

indexImpar = np.where(arr % 2 != 0) # O comando where, cria uma lista com os index do numero procurado
n_array = np.array(arr[indexImpar])
print(n_array)





print('\n'*5)
#Correção
arr = np.array([3,1,2,7,8,9,6,4,3]).reshape(3,3)
impar = (arr%2 != 0)
print(impar)
n_array = arr[impar]
print(n_array)







print('\n'*5)
# Exercício
# Pegar todos os impares e substituir por '-1'
arr = np.array([3,1,2,7,8,9,6,4,3]).reshape(3,3)
indexImpar = np.where(arr % 2 != 0)
arr[indexImpar] = -1
print(arr)






print('\n'*5)
arr = np.array([3,1,2,7,8,9,6,4,3]).reshape(3,3)
print(np.where((arr%2 !=0),-1,arr))


print(np.linspace(1,10,7, endpoint=False))













# Exercício Contar os elementos de um array
print('\n'*5*2)
arr = np.random.randint(1,11, size=(6,10))
print(arr)
x = np.arange(1,11)
lista = []

for i in range(6):
    for j in range(10):
        contador = 0
        for k in range(10):
            if arr[i][k] == x[j]:
                contador += 1
        lista.append(contador)
print(x)
print(np.array(lista).reshape(6,10))











