'''
Algoritmos em bionformatica
atividade 02 - exercicio 07
Nome: Daniel Puglisi
RA: 140355
'''

file = open('Seq_a.fasta', 'r')
j=0
dna=''
dna2=''
for i in file.readlines():
        j=j+1
        if(j>1):
           dna = dna + i

file2 = open('Seq_b.fasta','r')
j=0
for i in file2.readlines():
        j=j+1
        if(j>1):
           dna2 = dna2 + i
file.close()
file2.close()
cont=0
dna = dna.replace("\n", "")
dna2 = dna2.replace("\n", "")
for i in range(0,200):
    if(dna[i]!=dna2[i]):
        print('A posição {} foi trocado {} -- > {}'.format(i+1, dna[i], dna2[i]))
        cont=cont+1

print("O número de nucleotídeos diferentes é {}".format(cont))

