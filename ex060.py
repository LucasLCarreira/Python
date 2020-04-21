# Exercício Python 060
# Leia um número e mostre o fatorial (while e for)
n = int(input('Digite um número: '))
p = 1
c = 1
while c <= n:
    p = p * c
    c = c + 1
print('O fatorial de {} é igual a {}'.format(n,p))

for c in range (c, n+1):
    p = p * c
print('O fatorial de {} é igual a {}'.format(n,p))

from math import factorial
f = factorial(n)
print('{}! = {}'.format(n,f))

# Professor
n = int(input('Digite um número: '))
c = n
f = 1
while c > 0:
    f = f * c
    c = c - 1
print('{}! = {}'.format(n,f))
