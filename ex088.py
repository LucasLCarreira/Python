# Exercício Python 088
# Programa que ajude um jogador da mega sena a criar palpites
# Deve perguntar quantos jogos serao gerados e vai sortear 6 números entre 1 e 60, pra cada jogo
# Cadastrando tudo em uma lista composta
from random import sample
from time import sleep
palpites = []
jogo = []
print('=-=' * 12)
print(f'\033[1m{"MEGA SENA":^36}\033[m')
print('=-=' * 12)
qtde = int(input('Digite a quantidade de jogos: '))
print('-' * 36)
for j in range(0, qtde):
    jogo.append(sample(range(1,61),6))
    palpites.append(jogo[:])
    jogo.clear()
for p in range(0, qtde):
    print(f'Jogo {p + 1:2}: {palpites[p][0]}')
    sleep(1)
    print('-' * 36)


