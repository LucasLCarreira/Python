# Exercício Python 078
# Leia 5 valores numéricos e guarde em uma lista
# Mostre o maior, o menor e suas respectivas posições
lista = list()
maior = 0
menor = 0
for n in range(0, 5):
    lista.append(int(input(f'Digite o {n+1}º valor: ')))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
print(f'O menor valor é o {menor} e está nas posições:',end=' ')
for posicao,n in enumerate(lista):
    if n == menor:
        print(f'{posicao}',end=' ')
print(f'\nO maior valor é o {maior} e está nas posições:',end=' ')
for posicao,n in enumerate(lista):
    if n == maior:
        print(f'{posicao}',end=' ')










