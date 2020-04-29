# Exercício 096
# Programa que tenha função chamada AREA, que receba as dimensoes de um terreno retangular
# E mostre a área do terreno

def area(l,p):
    a = l * p
    print(f'A área do terreno de {l} m de largura por {p} m de profundidade é {a} m².')


l = float(input('Digite a largura do terreno: '))
p = float(input('Digite a profundidade do terreno: '))
area(l,p)