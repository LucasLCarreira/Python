# Exercício Python 016:
# Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira
from math import trunc
n = float(input('Digite um número qualquer: '))
print('A porção inteira de {} é {}!'.format(n,trunc(n)))