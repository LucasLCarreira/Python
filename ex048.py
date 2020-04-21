# Exercício Python 048
# Calcule a soma de todos números impares, multiplos de 3, no intervalo de 1 até 500
soma = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma = soma + c
print(soma)

# Resolução do professor
soma2 = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma2 = soma2 + c
print(soma2)