# Exercício Python 039
# LEIA O ANO DE NASCIMENTO E MOSTRE SE:
# AINDA VAI SE ALISTAR AO SERVICO MILITAR
# HORA DE SE ALISTAR
# JÁ PASSOU DO TEMPO
# DEVERA MOSTRAR TBM QUANTO TEMPO FALTA E QUANTO TEMPO PASSOU

from datetime import date
a = int(input("Qual é o ano de nascimento? "))
idade = date.today().year - a
if idade == 18:
    print('Você tem {} anos, está na hora de se alistar ao serviço militar!'.format(idade))
elif idade > 18:
    tempo = idade - 18
    print('Você tem {} anos e passou da idade de alistamento militar a {} anos.'.format(idade,tempo))
else:
    tempo = 18 - idade
    print('Você tem {} e ainda faltam {} anos para o alistamento militar.'.format(idade,tempo))
