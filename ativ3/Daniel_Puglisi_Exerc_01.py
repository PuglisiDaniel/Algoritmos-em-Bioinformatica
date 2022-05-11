'''
Algoritmos em bionformatica
atividade 03 - exercicio 01
Nome: Daniel Puglisi
RA: 140355
'''

def fatorial(n):
    fat=1
    for i in range(1,n+1):
        fat = fat*i

    print(fat)

n = int(input('Entre com o numero: '))

fatorial(n)

