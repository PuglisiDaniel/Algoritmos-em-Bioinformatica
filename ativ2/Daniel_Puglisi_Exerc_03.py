'''
Algoritmos em bionformatica
atividade 02 - exercicio 03
Nome: Daniel Puglisi
RA: 140355
'''

for i in range(1,6):
   if(i>=2):
       print('{}'.format(i), end=" ")
       for j in range(2, i+1):
        print('{}'.format(i*j), end=" ")
       print(' ')
   else:
       print(i)