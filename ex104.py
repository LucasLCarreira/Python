# Exercício 104
# Programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input do Python,
# só que fazendo a validação para aceitar apenas um valor numérico

def leiaInt(n):
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric() == True:
            print(f'Você digitou o número \033[1m{n}')
            break
        else:
            print(f'\033[1;31mErro! Digite um número inteiro!\033[m')

n = leiaInt('Digite um número: ')