# Exercício 095
# Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.
jogador = {}
gols = []
lista = []
somagol = 0
while True:
    jogador['Nome'] = str(input('Nome: ')).strip().title()
    jogador['Partidas'] = int(input('Quantidade de partidas: '))
    for j in range(1, jogador['Partidas'] + 1):
        gol = int(input(f'Quantos gols na partida {j}? '))
        gols.append(gol)
        somagol += gol
    jogador['Gols'] = gols
    jogador['Total'] = somagol
    lista.append(jogador.copy())
    gols = []
    somagol = 0
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print('=-=' * 15)
    if res == 'N':
        break
print('NUM  NOME        PARTIDAS  GOLS  MÉDIA\n'
      '---------------------------------------')
for d in range(0, len(lista)):
    print(f'{d+1:^3}  '
          f'{lista[d]["Nome"]:10}  '
          f'{lista[d]["Partidas"]:^8}  '
          f'{lista[d]["Total"]:^4}  '
          f'{lista[d]["Total"] / lista[d]["Partidas"]:4.2f}')
print('=-=' * 15)
while True:
    dados = int(input('Quer mostrar os dados de qual jogador? [999 para encerrar] '))
    if dados == 999:
        break
    if dados > len(lista):
        print('Dados inexistentes!')
    else:
        print('=-=' * 15)
        print(f'Levantamento do jogador {lista[dados - 1]["Nome"]}')
        p = 1
        for g in range(0, len(lista[dados - 1]["Gols"])):
            print(f'Partida {p}: {lista[dados - 1]["Gols"][g]} gols')
            p += 1
        print('=-=' * 15)
print('FIM')
