# Exercício Python 017
# Leia o comprimento dos catetos e calcule e mostre a hipotenusa
cA = int(input('Digite o cateto adjacente: '))
cO = int(input('Digite o cateto oposto: '))
h = (cA ** 2 + cO ** 2) ** 0.5
print('A hipotenusa é {}'.format(h))

from math import hypot
cA = int(input('Digite o cateto adjacente: '))
cO = int(input('Digite o cateto oposto: '))
h = hypot(cA,cO)
print('A hipotenusa é {}'.format(h))