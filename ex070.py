# Exercício Python 070
# Leia o nome e preço de varios produtos. Pergunte se quer continuar. Mostre:
# a: total gasto; b: quantos produtos custam > 1000; c: nome do produto mais barato

contador = 1
soma = mil = 0
barato = 0
nomebarato = ''
while True:
    print('·' * 35)
    print(f'Produto {contador}')
    produto = str(input('ITEM: ')).strip().upper()
    preco = float(input('PREÇO: R$ '))
    res = str(input('MAIS PRODUTOS [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('MAIS PRODUTOS [S/N]: ')).strip().upper()[0]
    soma += preco
    if preco > 1000:
        mil += 1
    if contador == 1 or preco < barato:
        barato = preco
        nomebarato = produto
    if res in 'N':
        break
    contador += 1
print('·' * 35)
print(f'TOTAL DA COMPRA: R$ {soma:.2f}')
print(f'EXISTEM {mil} PRODUTOS ACIMA DE R$ 1000,00.')
print(f'{nomebarato} É O PRODUTO MAIS BARATO E CUSTA R$ {barato:.2f}.')