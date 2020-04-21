# Exercício Python 063
# Leia um número inteiro e mostre os n primeiros elementos de uma sequencia de fibonacci
# ex 0 1 1 2 3 5 8
n = int(input('Digite um número: '))
a = 0
b = 1
c = 0
contador = 0
while contador < n:
    c = c + a
    a = b
    b = c
    print(c,end=' ')
    contador = contador + 1