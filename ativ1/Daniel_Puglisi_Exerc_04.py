'''
Algoritmos em bionformatica
atividade 01 - exercicio 04
Nome: Daniel Puglisi
RA: 140355
'''
cigarro = int(input('Quantos cigarros o senhor fuma por dia? '))
anos = int(input('Ja faz quantos anos que o senhor fuma? '))

totalCig = (anos*365*cigarro)
diasP = (totalCig*10)/(60*24)
print('O senhor perderá {} dias de vida se continuar nesta rotina'.format(diasP))



