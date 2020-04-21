# Exercício Python 054
# Leia o ano de nascimento de 7 pessoas.
# Quantas atingiram a maioridade e quantas não atingiram, m=21
from datetime import date
s = 0
for c in range(0,7):
    a = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - a
    if idade >= 21:
        s = s + 1
print('{} pessoas atingiram a maioridade de 21 anos!'.format(s))
print('{} pessoas não atingiram a maioridade de 21 anos!'.format(7-s))
