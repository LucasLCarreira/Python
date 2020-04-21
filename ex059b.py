# Exercício Python 059
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    print('=' * 30)
    escolha = int(input('Digite o que quer fazer:\n'
                        '[1] Somar\n'
                        '[2] Multiplicar\n'
                        '[3] Verificar qual é o maior\n'
                        '[4] Inserir novos valores\n'
                        '[5] Sair do programa\n'))
    if escolha == 1:
        soma = a + b
        print('A soma de {} + {} é {}'.format(a, b, soma))
    elif escolha == 2:
        produto = a * b
        print('O produto de {} x {} é {}'.format(a, b, produto))
    elif escolha == 3:
        if a > b:
            maior = a
        else:
            maior = b
        print('O maior valor é {}.'.format(maior))
    elif escolha == 4:
        a = int(input('Digite o primeiro valor: '))
        b = int(input('Digite o segundo valor: '))
print('FIM')
