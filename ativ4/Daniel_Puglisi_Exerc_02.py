'''
Algoritmos em bionformatica
atividade 04 - exercicio 02
Nome: Daniel Puglisi
RA: 140355
'''


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 150)
y = np.sin(x)
z = np.cos(x)
k = np.tan(x)

plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
plt.plot(x, y,'r', linewidth=1)
plt.title('funcao seno(x)')
plt.xlim((-6, 6))
plt.ylim((-1.1, 1.1))
plt.subplot(2,2,2)
plt.title('funcao cos(x)')
plt.bar(x,z)
plt.subplot(2,2,3)
plt.title('funcao tg(x)')
plt.xlabel('valor de x')
plt.plot(x, k, 'o')
plt.ylim((-40,40))

plt.show()

