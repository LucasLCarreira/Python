# Exercício Python 015:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Digite a qtde de dias alugados: '))
km = float(input('Digite a qtde de km rodados: '))
pd = 60
pkm = 0.15
p = (d * pd) + (km * pkm)
print('O preço a pagar é: R$ {:.2f}'.format(p))
