# Exercício Python 042
# 3 RETAS FORMAM UM TRIANGULO? SE SIM:
# EQUILATERO, ISOSCELES OU ESCALENO
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    if a == b and a == c:
        print('As retas formam um triângulo equilátero!')
    elif a != b and a != c and b != c:
        print('As retas formam um triângulo escaleno!')
    else:
        print('As retas formam um triângulo isósceles!')
else:
    print('As retas não formam um triângulo!')
