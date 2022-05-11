'''
Algoritmos em bionformatica
atividade 04 - exercicio 01-a)
Nome: Daniel Puglisi
RA: 140355
'''

import numpy as np
import matplotlib.pyplot as plt

n = int(input('numero de pontos: '))
x = np.random.rand(n)
y = np.random.rand(n)

plt.scatter(x, y)
plt.title('Monte Carlo calculo de PI')
plt.xlabel('raio')
plt.ylabel('raio')
plt.xlim((0, 1.1))
plt.ylim((0, 1.1))
aux = x*x + y*y < 1
pi = 4*aux.sum()/n
print(pi)
plt.show()

