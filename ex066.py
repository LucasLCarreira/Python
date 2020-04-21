# Exercício Python 066
# Leia varios números inteiros. Só para quando digitar 999
# Mostre quantos números foram inseridos e a soma entre eles.

contador = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma = soma + n
    contador = contador + 1
print(f'Foram digitados {contador} números e a soma entre eles é {soma}.')