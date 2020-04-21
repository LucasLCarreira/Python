# Exercício Python 041
# LEIA ANO DE NASCIMENTO DO ATLETA E MOSTRE A CATEGORIA
# ATÉ 9 ANOS: MIRIM
# ATÉ 14 ANOS: INFANTIL
# ATÉ 19 ANOS: JUNIOR
# ATÉ 25 ANOS: SENIOR
# ACIMA: MASTER
from datetime import date
ano = int(input("Qual é o ano de nascimento do atleta? "))
idade = date.today().year - ano
if idade <= 9:
    print('O atleta tem {} anos e está na categoria MIRIM!'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e está na categoria INFANTIL!'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e está na categoria JUNIOR!'.format(idade))
elif idade <=25:
    print('O atleta tem {} anos e está na categoria SENIOR!'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria MASTER!'.format(idade))