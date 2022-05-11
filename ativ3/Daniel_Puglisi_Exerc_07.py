'''
Algoritmos em bionformatica
atividade 03 - exercicio 07
Nome: Daniel Puglisi
RA: 140355
'''

import numpy as np
import math

matrix = np.random.randint(-10, 66, (4, 5))

#a
absoluto = np.absolute(matrix)
print('O valor absoluto:\n{}\n'.format(absoluto))

#b
aux = matrix[0,:]
linha = np.sin(aux)
print('O seno dos valores contidos na primeira linha: \n{}\n'.format(linha))
#c
print('Numeros maximos das colunas:\n{}\n'.format(matrix.max(0)))
#d
print('Soma das colunas:\n{}\n'.format(matrix.sum(0)))
#e
print('Soma das linhas:\n{}\n'.format(matrix.sum(1)))
#f

print('Produto de cada coluna (passo a passo):\n{}\n'.format(matrix.cumprod(0)))




