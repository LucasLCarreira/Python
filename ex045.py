# Exercício Python 045
# CRIE UM PROGRAMA QUE FACA O COMPUTADOR JOGAR JOKENPO COM VC
import random
import time
import emoji
jogador = int(input('\033[1;34mVamos jogar Jokenpô!\n'
                    'Escolha:\n'
                    '\033[1;31m[1] Papel\n'
                    '\033[1;35m[2] Pedra\n'
                    '\033[1;36m[3] Tesoura\033[m\n'
                    '\033[1;34mVocê escolheu: \033[m'))

computador = random.randint(1,3)

if jogador != 1 and jogador != 2 and jogador != 3:
    print('\033[1;34mEscolha um dos seguintes valores: 1, 2 ou 3!\033[m')

if computador == 1:
    if jogador == 1:
        print('\033[1mPROCESSANDO...')
        time.sleep(2)
        print('\033[1;34mEmpate! Você e o Computador escolheram \033[1;31mPapel\033[1;34m!')
    elif jogador == 2:
        print('\033[1mPROCESSANDO...')
        time.sleep(2)
        print('\033[1;35mVocê perdeu! \033[1;31mPapel\033[1;34m embrulha \033[1;35mPedra\033[1;34m!')
    elif jogador == 3:
        print('\033[1mPROCESSANDO...')
        time.sleep(2)
        print('\033[1;36mVocê venceu! \033[1;36mTesoura\033[1;34m corta \033[1;31mPapel\033[1;34m!')

if computador == 2:
    if jogador == 1:
        print('\033[1mPROCESSANDO...')
        time.sleep(2)
        print('\033[1;36mVocê venceu! \033[1;31mPapel\033[1;34m embrulha \033[1;35mPedra\033[1;34m!')
    elif jogador == 2:
        print('\033[1mPROCESSANDO...')
        time.sleep(2)
        print('\033[1;34mEmpate! Você e o Computador escolheram \033[1;35mPedra\033[1;34m!')
    elif jogador == 3:
        print('\033[1mPROCESSANDO...')
        time.sleep(2)
        print('\033[1;35mVocê perdeu! \033[1;35mPedra\033[1;34m quebra \033[1;36mTesoura\033[1;34m!')

if computador == 3:
    if jogador == 1:
        print('\033[1mPROCESSANDO...')
        time.sleep(2)
        print('\033[1;35mVocê perdeu! \033[1;36mTesoura\033[1;34m corta \033[1;31mPapel\033[1;34m!')
    elif jogador == 2:
        print('\033[1mPROCESSANDO...')
        time.sleep(2)
        print('\033[1;36mVocê venceu! \033[1;35mPedra\033[1;34m quebra \033[1;36mTesoura\033[1;34m!')
    elif jogador == 3:
        print('\033[1mPROCESSANDO...')
        time.sleep(2)
        print('\033[1;34mEmpate! Você e o Computador escolheram \033[1;36mTesoura\033[1;34m')
