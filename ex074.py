# Exercício Python 074
# Crie um programa que gere 3 números aleatórios e colocar em uma tupla
# Depois, mostre a listagem de números gerados e indique o menor e maior valor da tupla

from random import randint
a= randint(1,10)
b= randint(1,10)
c= randint(1,10)
numeros = (a, b, c)
print(f'Os números sorteados foram: ',end='')
for n in numeros:
    print(f'{n}',end=' ')
print(f'\nO maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')