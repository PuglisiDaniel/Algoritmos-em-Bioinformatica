'''
Algoritmos em bionformatica
atividade 03 - exercicio 04
Nome: Daniel Puglisi
RA: 140355
'''

pessoas = dict()
listPessoa = list()

n = int(input('Quantas pessoas deseja cadastrar? '))
mediaP = mediaA = mediaIMC = 0
for i in range(0,n):
    pessoas['Nome'] = str(input('Entre com o nome: '))
    pessoas['Sexo'] = str(input('Entre com o sexo: '))
    pessoas['Peso'] = float(input('Entre com o peso: '))
    pessoas['Altura'] = float(input('Entre com a altura: '))

    pessoas['IMC'] = pessoas['Peso'] / (pessoas['Altura'] * pessoas['Altura'])

    mediaP=mediaP+pessoas['Peso']
    mediaA = mediaA + pessoas['Altura']
    mediaIMC = mediaIMC + pessoas['IMC']

    listPessoa.append(pessoas.copy())
    print()


print(f'\nForam cadastradas {n} pessoas ')

print('A média de peso das pessoas foi {:.2f}Kg\n'
      'A media de altura das pessoas foi {:.2f}m\n'
      'A média de IMC das pessoas foi {:.2f}\n'.format(mediaP/n, mediaA/n, mediaIMC/n))

print(listPessoa)


