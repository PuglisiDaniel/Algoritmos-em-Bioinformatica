'''
Algoritmos em bionformatica
atividade 02 - exercicio 06
Nome: Daniel Puglisi
RA: 140355
'''

file = open('Corona_genomic.fasta', 'r')
j=0
corona=''
for i in file.readlines():
        j=j+1
        if(j>1):
           corona = corona + i


file.close()
mod = corona.replace('T', 'a')
mod = mod.replace('A', 't')
mod = mod.replace('C', 'g')
mod = mod.replace('G', 'c')
mod = mod.upper()
print(mod)

file2 = open('ex07_a.txt', 'w')
file2.writelines(mod)

file2.close()

