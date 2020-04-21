# Exercício Python 010:
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
x = float(input('Digite o valor que uma pessoa tem na carteira em reais: '))
d = 3.27
print('A pessoa pode comprar {:.2f} dolares'.format(x/d))
