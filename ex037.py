# Exercício Python 037
# LEIA UM NÚMERO INTEIRO QUALQUER E PECA PARA O USUARIO ESCOLHER
# A BASE DE CONVERSAO: 1-BINARIO; 2-OCTAL; 3-HEXADECIMAL
import binhex

n = int(input('Digite um número: '))
opcao = int(input('Esolha uma das bases para conversão:\n'
      '[1] Binário\n'
      '[2] Octal\n'
      '[3] Hexadecimal\n'))

if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(n,bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
        print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')