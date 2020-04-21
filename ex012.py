# Exercício Python 012:
# Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preço atual: '))
print('O preço com desconto é R$ {:.2f}'.format(p*0.95))
