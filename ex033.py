# Exercício Python 033
# Leia 3 números e mostre qual é o menor e o maior

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2:
    if n1 > n3:
        print('{} é o maior!'.format(n1))
        if n2 > n3:
            print('{} é o menor!'.format(n3))
        else:
            print('{} é o menor!'.format(n2))
    else:
        print('{} é o maior!'.format(n3))
        print('{} é o menor!'.format(n2))
else:
    if n2 > n3:
        print('{} é o maior!'.format(n2))
        if n1 > n3:
            print('{} é o menor!'.format(n3))
        else:
            print('{} é o menor!'.format(n1))
    else:
        print('{} é o maior!'.format(n3))
        print('{} é o menor!'.format(n1))

# Resolução do professor
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor'))
menor = a  # se o A for o menor já eliminou etapas
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))
