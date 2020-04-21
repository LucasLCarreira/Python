# Exercício Python 038
# LEIA 2 NUMEROS INTEIROS. MOSTRE MAIOR, MENOR OU IGUAL
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
if a > b:
    print('O maior número é o {}!'.format(a))
    print('O menor número é o {}!'.format(b))
elif a < b:
    print('O maior número é o {}!'.format(b))
    print('O menor número é o {}!'.format(a))
else:
    print('Não existe maior ou menor, {} e {} são iguais!'.format(a, b))
