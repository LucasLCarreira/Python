# Exercício Python 064
# Leia varios numeros inteiros. Programa para quando digita 999
# No final, mostra quantos números foram digitados
# A soma entre eles, desconsiderando o flag (999)
soma = c = n = 0
while n != 999:
    soma = soma + n
    c = c + 1
    n = int(input('Digite um número: '))
print('Você digitou {} números e a soma é {}.'.format(c - 1, soma))
