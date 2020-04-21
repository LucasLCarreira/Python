# Exercício Python 071
valor = int(input('Digite o valor do saque: '))
total = valor
cinquenta = vinte = dez = um = 0
while total >= 50:
    total -= 50
    cinquenta += 1
while total >= 20:
    total -= 20
    vinte += 1
while total >= 10:
    total -= 10
    dez += 1
while total >= 1:
    total -= 1
    um += 1
print(f'Notas de R$ 50: {cinquenta}')
print(f'Notas de R$ 20: {vinte}')
print(f'Notas de R$ 10: {dez}')
print(f'Notas de R$ 01: {um}')
