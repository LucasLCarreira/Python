# Exercício Python 011:
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
a = l * h
r = 2
print('A área da parede é {} m²'.format(a))
print('A quantidade de tinta necessária é {:.2f} litros'.format(a/r))

