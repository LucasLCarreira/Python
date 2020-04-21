# Exercício Python 028
# Escreva um programa que faça o computador pensar em um número entre 0 e 5
# e peça para o usuário tentar descobrir o número escolhido pelo computador.
# Mostre se o usuário venceu ou perdeu.

import random
n = int(input('O computador escolheu um número de 0 a 5. Tente adivinhar! '))
lista = [0,1,2,3,4,5]
e = random.choice(lista)
if n==e:
    print('Parabéns, você acertou! O número escolhido foi {}'.format(e))
else:
    print('Não foi dessa vez! O número escolhido foi {}'.format(e))
print('_'*60)

#resolução do professor
from random import randint
from time import sleep
computador = randint(0,5) # Sorteia um número de 0 a 5
n = int(input('O computador escolheu um número de 0 a 5. Tente adivinhar! '))
print('Processando...')
sleep(2)
if n == computador:
    print('Parabéns, você acertou! O número escolhido foi {}'.format(computador))
else:
    print('Não foi dessa vez! O número escolhido foi {}'.format(computador))
