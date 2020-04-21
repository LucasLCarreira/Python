# Exercício Python 059
# Leia 2 valores e mostre um menu
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

maior = 0
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
escolha = int(input('Digite o que quer fazer:\n'
                    '[1] Somar\n'
                    '[2] Multiplicar\n'
                    '[3] Verificar qual é o maior\n'
                    '[4] Inserir novos valores\n'
                    '[5] Sair do programa\n'))
while escolha == 4:
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    escolha = int(input('Digite o que quer fazer:\n'
                        '[1] Somar\n'
                        '[2] Multiplicar\n'
                        '[3] Verificar qual é o maior\n'
                        '[4] Inserir novos valores\n'
                        '[5] Sair do programa\n'))
if escolha == 1:
    print('A soma de {} e {} é igual a {}'.format(a, b, a + b))
elif escolha == 2:
    print('A multiplicação de {} e {} é igual a {}'.format(a, b, a * b))
elif escolha == 3:
    if a > b:
        maior = a
        print('O maior valor é {}'.format(a))
    elif b > a:
        maior = b
        print('O maior valor é {}'.format(b))

print('FIM')
if b > maior:
    print(b)