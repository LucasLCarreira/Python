# Exercício Python 051
# Leia o primeiro termo e a razão de uma progressão aritmética
# Mostre os 10 primeiros termos dessa progressão
n = int(input('Digite o primeiro termo: '))
p = int(input('Digite a constante de progressão: '))
for c in range(n,10,p):
    print('{}·'.format(c),end='')
print('FIM')
# Professor
n = int(input('Digite o primeiro termo: '))
p = int(input('Digite a constante de progressão: '))
t = 10 * p + n
for c in range(n, t, p):
    print('{}·'.format(c),end='')
print('FIM')
