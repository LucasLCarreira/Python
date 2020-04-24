# Exercício 093
# Programa que gerencie o aproveitamento de um jogador de futebol
# O programa vai ler o nome, qtde de partidas, quantos gols em cada partida
# Guardar tudo em um dicionário, incluindo total de gols feitos durante um campeonato
jogador = {}
gols = []
somagol = 0
jogador['Nome'] = str(input('Nome: ')).strip().title()
jogador['Partidas'] = int(input('Quantidade de partidas: '))
for j in range(1, jogador['Partidas'] + 1):
    gol = int(input(f'Quantos gols na partida {j}? '))
    gols.append(gol)
    somagol += gol
jogador['Gols'] = gols
jogador['Total'] = somagol
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for j in range(1, jogador['Partidas'] + 1):
    print(f'    => Na partida {j}: {gols[j - 1]} gols')
print(f'Foi um total de {jogador["Total"]} gols.')

# resolução do professor
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')