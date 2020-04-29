# Exercício 103
# Programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome do jogador e quantos gols ele marcou. O programa deverá mostrar a ficha do jogador,
# mesmo que algum dado tenha sido informado incorretamente

def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s).')


n = str(input('Nome do jogador: ')).strip().title()
g = str(input('Número de gols: ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gol=g)
else:
    ficha(n, g)