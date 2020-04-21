# Exercício Python 052
# Leia um número inteiro e diga se ele é primo ou não

n = int(input('Digite um número: '))
divisor = 2
soma = 0
while divisor < n:
    if n % divisor != 0:
        soma = soma + 1
    divisor += 1
if soma == n - 2:
    print('{} é primo, pois é divisível por apenas {} números!'.format(n,n-soma))
else:
    print('{} não é primo, pois é divisível por {} números!'.format(n,n-soma))
'''
# Resolução do professor
num = int(input('Digite um número: '))
total = 0
for c in range(1,num + 1):
    if num % c == 0:
        print('\033[33m',end='')
        total += 1
    else:
        print('\033[31m',end='')
    print('{}'.format(c),end='')
print('\n\033[mO número {} é divisível {} vezes'.format(num,total))
if total == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')
'''