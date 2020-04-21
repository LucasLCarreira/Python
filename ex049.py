# Exercício Python 049
# Refaça o desafio 009, tabuada utilizando o FOR
n = int(input('Digite um número: '))
for c in range(1,11):
    print('{:2} x {:2} = {:2}'.format(n,c,c*n))
