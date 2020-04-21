# Exercício Python 058
# Melhore o jogo 28 onde o computador vai pensar em um número de 0 a 10
# Jogador vai tentar adivinhar até acertar, mostrando quantos palpites

import random
computador = random.randint(0,10)
soma = 0
jogador = 0
while jogador != computador:
    jogador = int(input('Tente advinhar! \n'))
    soma = soma + 1
print('Você acertou em {} tentativas!'.format(soma))

# Professor
from random import randint
computador = randint(0,10)
print('Seu adversário pensou em um número de 0 a 10.')
print('Será que você consegue adivinhar?')
acerto = False
soma = 0
while not acerto: # igual a while acerto == False
    jogador = int(input('Qual é o seu palpite? '))
    soma = soma + 1
    if jogador == computador:
        acerto = True
print('Acertou em {} tentativas!'.format(soma))

# Professor (com facilitador)
from random import randint
computador = randint(0,10)
print('Seu adversário pensou em um número de 0 a 10.')
print('Será que você consegue adivinhar?')
acerto = False
soma = 0
while not acerto: # igual a while acerto == False
    jogador = int(input('Qual é o seu palpite? '))
    soma = soma + 1
    if jogador == computador:
        acerto = True
    else:
        if jogador < computador:
            print('Dica, o número é maior!')
        else:
            print('Dica, o número é menor')
print('Acertou em {} tentativas!'.format(soma))