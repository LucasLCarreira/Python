# Exercício Python 085
# Programa que o usuario possa digita 7 valores e cadastre-os em uma lista
# que mantenha separados os valores pares e ímpares. Mostre os pares e ímpares em ordem.
pares = []
impares = []
numeros = []
for v in range(0,7):
    n = int(input(f'Digite o {v+1}º número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
numeros.append(pares[:])
numeros.append(impares[:])
pares.sort()
impares.sort()
print(f'Os números pares são: {pares}\n'
      f'Os números impares são: {impares}\n'
      f'E a lista de números é: {numeros}')

