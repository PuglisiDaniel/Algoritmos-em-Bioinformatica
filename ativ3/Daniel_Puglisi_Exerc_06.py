'''
Algoritmos em bionformatica
atividade 03 - exercicio 06
Nome: Daniel Puglisi
RA: 140355
'''

import numpy as np
import math

vetor = np.array([5.2,6,7,8,20,1])
print(vetor)
tam = vetor.size
par = list()

for i in range(0, tam):
    if(vetor[i]%2==0):
        par.append(vetor[i])

print(par)
