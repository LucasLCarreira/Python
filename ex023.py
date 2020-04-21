# Exercício Python 023
# Leia um número de 0 a 9999 e mostre os digitos separados (milhar, centena, dezena, unidade)
# usando matemática
n = int(input('Digite um número de 0 a 9999: '))
u = n % 10
print('Unidade: {}'.format(u))
a = n - u
d = (a % 100)
print('Dezena: {}'.format(d//10))
b = a - d
c = (b % 1000)
print('Centena: {}'.format(c//100))
m = (n - c - d - u)
print('Milhar: {}'.format(m//1000))

# usando string

n = (input('Digite um número de 0 a 9999: '))
print('{:>3}'.format(n[0]),'milhar(es)')
print('{:>3}'.format(n[1]),'centena(s)')
print('{:>3}'.format(n[2]),'dezena(s)')
print('{:>3}'.format(n[3]),'unidade(s)')

