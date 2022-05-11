'''
Algoritmos em bionformatica
atividade 02 - exercicio 04
Nome: Daniel Puglisi
RA: 140355
'''

dna = input('Entre com a sequência de DNA: ')
decide = 1
tam=len(dna)

for i in range(0, tam):
    if(dna[i]!= 'C' and dna[i]!= 'A' and dna[i]!= 'T' and dna[i]!= 'G' ):
        decide = 0

if decide != 0:
    print('A sequencia digitada é valida')

    print('O numero total de nucleotideos da sequencia digitada é: {}'.format(len(dna)))
    print('A sequencia digitada possui:\n'
          '{} - Adenina(A)\n'
          '{} - Guanina(G)\n'
          '{} - Citosina(C)\n'
          '{} - Timina(T)\n'.format(dna.count('A'),dna.count('G'),dna.count('C'),dna.count('T')))

    A =float((dna.count('A')*100)/tam)
    G =float((dna.count('G')*100)/tam)
    C =float((dna.count('C')*100)/tam)
    T =float((dna.count('T')*100)/tam)

    print('{:.2f}% Adenina(A)\n'
          '{:.2f}% Guanina(G)\n'
          '{:.2f}% Citosina(C)\n'
          '{:.2f}% Timina(T)'.format(A, G, C, T))

else:
    print('A sequencia digitada é invalida')
