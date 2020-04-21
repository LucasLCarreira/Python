# Exercício Python 075
# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. Mostre:
# A - Quantas vezes aparece o valor 9
# B - Em que posição foi digitado o primeiro valor 3
# C - Quais foram os números pares
n1 = int(input('Digite o primeiro número:   '))
n2 = int(input('Digite o segundo número:    '))
n3 = int(input('Digite o terceiro número:   '))
n4 = int(input('Digite o quarto número:     '))
tupla = (n1, n2, n3, n4)
print(f'Você digitou os valores {tupla}')
# ITEM A
if 9 not in tupla:
    print(f'O valor 9 não apareceu nenhuma vez.')
else:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
# ITEM B
if 3 not in tupla:
    print(f'O valor 3 não apareceu em nenhuma posição.')
else:
    tres = tupla.index(3)
    print(f'O valor 3 apareceu na {tres}ª posição.')
# ITEM C
print(f'Os valores pares são:',end=' ')
impares = 0
for c in tupla:
    if c % 2 == 0:
        print(c,end=' ')
    else:
        impares += 1
if impares == len(tupla):
    print('Nenhum!')

