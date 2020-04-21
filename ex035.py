# Exercício Python 035
# Leia o comprimento de 3 retas e diga se elas podem ou nao formar um triangulo

a = int(input('Digite a reta 1: '))
b = int(input('Digite a reta 2: '))
c = int(input('Digite a reta 3: '))
if (b - c) < a and (b + c) > a:
    if (a - c) < b and (a + c) > b:
        if (a - b) < c and (a + b) > c:
            print('É possível formar um triangulo!')
        else:
            print('Não é possível formar um triangulo!')
# Resolução do professor
a = int(input('Digite a reta 1: '))
b = int(input('Digite a reta 2: '))
c = int(input('Digite a reta 3: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triangulo!')
else:
    print('Não é possível formar um triangulo!')