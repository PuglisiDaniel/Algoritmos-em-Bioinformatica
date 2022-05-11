'''
Algoritmos em bionformatica
atividade 02 - exercicio 02
Nome: Daniel Puglisi
RA: 140355
'''

depInicial = float(input('Entre com o deposito inicial: '))
taxa = float(input('Entre com a taxa de juros da poupança(%): '))

conv = (depInicial*taxa)/100 #coversao da taxa de porcento em dinheiro
montante=depInicial
for i in range(0,24):
    print('{}º mês - R${}'.format(i+1, montante+conv))
    montante = montante + conv

print('\nO total de ganho com juros no periodo de 24 meses foi: R${}'.format(montante-depInicial))