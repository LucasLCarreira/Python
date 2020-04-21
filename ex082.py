# Exercício Python 082
# Crie um programa que vai ler vários números e coloque-os em uma lista
# Depois, crie duas listas extras que vão conter apenas os valores pares e impares
# Ao final, mostre o conteúdo das 3 listas geradas
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    res = str(input('Quer continuar? [S/N] ')).strip().upper()
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res == 'N':
        break
print(f'A lista é {lista}')
pares = []
impares = []
for n in range(0, len(lista)):
    if lista[n] % 2 == 0:
        pares.append(lista[n])
    else:
        impares.append(lista[n])

print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')