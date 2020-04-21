# Exercício Python 081
# Crie um programa que vai ler vários números e colocar em uma lista. Mostre:
# A - Quantos números digitados
# B - A lista de valores em ordem decrescente
# C - Se o valor 5 foi digitado e está na lista ou não
numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    res = str(input('Quer continuar? [S/N] ')).strip().upper()
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res == 'N':
        break
numeros.sort(reverse=True)
print(f'A lista é: {numeros}.')
print(f'Foram digitados {len(numeros)} números.')
if 5 in numeros:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
