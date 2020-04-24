# Exercício 091
# Programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# Coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
from random import randint
dado = {}
for d in range(1, 5):
    dado[f'Jogador {d}'] = randint(1,6)
print('Valores sorteados')
for k, v in dado.items():
    print(f'{k}: {v}')
n = 6
p = 1
while True:
    for k, v in dado.items():
        if v == n:
            print(f'{p}º lugar: {k} ({v} pontos)')
            p += 1
    n -= 1
    if n == 0:
        break
# Resolução do professor
print('=-=' * 20)
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = []
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# itemgetter - (0): seleciona as chaves (1): seleciona os valores
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)




