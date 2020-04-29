# Exercício 100
# Programa que tenha uma lista chamada NUMEROS e duas funções: SORTEIA() e SOMAPAR().
# A primeira vai sortear 5 números e colocá-los dentros da lista
# A segunda mostra a soma dos valores pares sorteados pela função anterior.

from random import randint

lista = []


def sorteia(lista):
    for c in range(0, 5):
        numero = randint(1, 100)
        lista.append(numero)
    print(f'Os números sorteados foram {lista}')


def somapar(lista):
    soma = 0
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f'A soma dos pares é {soma}')


sorteia(lista)
somapar(lista)
