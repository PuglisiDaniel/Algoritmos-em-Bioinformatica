'''
Algoritmos em bionformatica
atividade 01 - exercicio 06
Nome: Daniel Puglisi
RA: 140355
'''

largura = float(input('Entre com largura em m: '))
altura = float(input('Entre com altura em m: '))

areaParede=largura*altura
qtdTinta=areaParede/3;

print('Serão necessários {} litros de tinta para pintar a area de {} m^2'.format(qtdTinta, areaParede))



