'''
Algoritmos em bionformatica
atividade 02 - exercicio 05
Nome: Daniel Puglisi
RA: 140355
'''

file = open('Corona_genomic.fasta', 'r')
j=0
for i in file.readlines():
        j=j+1
        if(j>1):
            print(i, end='')
file.close()