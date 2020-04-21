# Exercício Python 068
# Jogo PAR ou IMPAR com o computador. O jogo será interrompido quando o jogador perder.
# Mostrar total de vitórias.
from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-='*10)
vitoria = 0
while True:
    computador = randint(1, 2)
    jogador = int(input('Escolha um número: '))
    tipo = str(input('PAR ou ÍMPAR? ')).strip().upper()[0]
    while tipo not in 'PIÍ':
        tipo = str(input('PAR ou ÍMPAR? ')).strip().upper()[0]
    resultado = jogador + computador
    if tipo in 'P':
        if resultado % 2 == 0:
            print(f'{resultado} é par! Você ganhou!')
            print('=-=' * 10)
            vitoria = vitoria + 1
        else:
            print(f'{resultado} é ímpar! Você perdeu!')
            print('=-=' * 10)
            break
    if tipo in 'IÍ':
        if resultado % 2 == 0:
            print(f'{resultado} é par! Você perdeu!')
            print('=-=' * 10)
            break
        else:
            print(f'{resultado} é ímpar! Você ganhou!')
            print('=-=' * 10)
            vitoria = vitoria + 1
print(f'Você ganhou {vitoria} vitórias consecutivas!')