'''
Algoritmos em bionformatica
atividade 03 - exercicio 03
Nome: Daniel Puglisi
RA: 140355
'''

def multiplo(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False


n1=int(input('Entre com o primeiro numero: '))
n2=int(input('Entre com o segundo numero: '))

print(multiplo(n1, n2))
