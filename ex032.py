# Exercício Python 032
# Leia um ano qualquer e mostre se é bissexto.

a = int(input('Digite um ano: '))
if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
    print('É bissexto!')
else:
    print('Não é bissexto')


from datetime import date
a = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual '))
if a == 0:
    ano = date.today().year
if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
    print('É bissexto!')
else:
    print('Não é bissexto')