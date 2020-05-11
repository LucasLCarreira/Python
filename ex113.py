# Reescreva a função leiaInt() que fizemos no desafio 104
# incluindo a possibilidade da digitação de um número de tipo inválido
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade


def leiaInt(n):
    while True:
        try:
            n = int(input('Digite um número inteiro:\n'))
        except Exception as erro:
            print(f'\033[1;31mERRO: {erro}\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO USUÁRIO PREFERIU NÃO INFORMAR OS DADOS!\033[m')
        else:
            print(f'Você digitou o número {n}!')
            break
        finally:
            print('FIM')


def leiaFloat(n):
    while True:
        try:
            n = float(input('Digite um número decimal:\n').replace(',','.'))
        except Exception as erro:
            print(f'ERRO: {erro}')
        except KeyboardInterrupt:
            print('O USUÁRIO PREFERIU NÃO INFORMAR OS DADOS!')
        else:
            print(f'Você digitou o número {n:.2f}!')
            break
        finally:
            print('FIM')


x = leiaInt('Digite um número inteiro: ')
y = leiaFloat('Digite um número decimal: ')