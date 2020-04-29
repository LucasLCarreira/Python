# Exercício 106
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará
# OBS: Use cores
def interactiveHelp():
    while True:
        cabecalho = 'SISTEMA DE AJUDA PyHELP'
        print('\033[7;30m=\033[m' * 75)
        print(f'\033[7;30m{cabecalho:^75}\033[m')
        print('\033[7;30m=\033[m' * 75)
        comando = str(input('\033[1mFUNÇÃO OU BIBLIOTECA > \033[m')).lower().strip()
        if comando.upper() == 'FIM':
            break
        acesso = f'Acessando o manual de comando {comando}'
        print('\033[1;43m=\033[m' * 75)
        print(f'\033[1;43m{acesso:^75}\033[m')
        print('\033[1;43m=\033[m' * 75)
        help(comando)

interactiveHelp()

