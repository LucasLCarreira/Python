# Exercício Python 031
# Desenvolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 para até 200km
# e R$ 0,45 para viagens mais longas

d = int(input('Qual é a distância da viagem? '))
if d <=200:
    p = d * 0.5
    print('O preço da passagem é R$ {:.2f}'.format(p))
else:
    p = d * 0.45
    print('O preço da passagem é R$ {:.2f}'.format(p))