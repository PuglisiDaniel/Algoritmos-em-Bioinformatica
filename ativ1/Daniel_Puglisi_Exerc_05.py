'''
Algoritmos em bionformatica
atividade 01 - exercicio 05
Nome: Daniel Puglisi
RA: 140355
'''
dia = int(input('Entre com os dias: '))
hora = int(input('Entre com as horas: '))
min = int(input('Entre com os minutos: '))
seg = int(input('Entre com os segundos: '))

result= seg+(min*60+(hora*60**2+(dia*24)*60**2))

print(result,'segundos totais')

