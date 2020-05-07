# Exercício 107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas:
# aumenta(), dminuir(), dobro() e metade.
# Faça um programa que importe esse módulo e use alguma dessas funções

from EX107 import moeda

p = float(input('Digite o preço: '))
print(f'Metade: R$ {moeda.metade(p)}')
print(f'Dobro: R$ {moeda.dobro(p)}')
print(f'Aumento: R$ {moeda.aumento(p, 10)}')
print(f'Redução: R$ {moeda.reducao(p, 13)}')