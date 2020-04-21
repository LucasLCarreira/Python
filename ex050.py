# Exercício Python 050
# Leia 6 números inteiros e mostre a soma dos pares
soma = 0
for c in range(1,7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares é: {}'.format(soma))