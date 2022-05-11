'''
Algoritmos em bionformatica
atividade 03 - exercicio 02
Nome: Daniel Puglisi
RA: 140355
'''

def maxnum(*lista):
    maior=lista[0]
    for i in lista:
        if i>maior:
            maior=i

    return  maior

print(maxnum(1,3,8,2))
print(maxnum(5,3,8,10,9))
print(maxnum(7,3,0,2,1,4))