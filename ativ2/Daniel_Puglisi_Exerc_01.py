'''
Algoritmos em bionformatica
atividade 02 - exercicio 01
Nome: Daniel Puglisi
RA: 140355
'''

primeiro = int(input('Entre com o primeiro número de uma PA: '))
razao = int(input('Entre com a razão da PA: '))

for i in range(0,10):
    print('{}º termo - {}'.format(i+1, primeiro+(i*razao)))

