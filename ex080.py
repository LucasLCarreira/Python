# Crie um programa onde o usuário possa digitar cinco valores númericos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort)
# Mostre a lista ordenada
'''
lista = []
for n in range(0,5):
    num = int(input('Digite um número: '))
    lista.append(num)
for contadorA in range(0,4):
    for contadorB in range(contadorA + 1, 5):
        if lista[contadorA] > lista[contadorB]:
            aux = lista[contadorB]
            lista[contadorB] = lista[contadorA]
            lista[contadorA] = aux
print(lista)'''

# Resolução do professor
lista = []
for n in range(0,5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > lista[-1]: # -1 comprimento da lista: len(lista) - 1
        lista.append(num)
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao += 1
print(lista)
