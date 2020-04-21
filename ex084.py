# Exercício Python 084
# Programa que leia nome e peso de varias pessoas, guardando em uma lista
# A - Quantas pessoas cadastradas
# B - Pessoas mais pesadas (peso e pessoa) +100
# C - Pessoas mais leves (peso e pessoa) -70

cadastro = []
maior = menor = 0
while True:
    cadastro.append([input('\nNome: '), float(input('Peso: '))][::-1])
    res = ''
    while res == '' or res[0] not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()
    if res[0] == 'N':
        break
print(f'\nForam cadastradas {len(cadastro)} pessoas.')
for m in [['Maior', max(cadastro)[0]], ['Menor', min(cadastro)[0]]]:
    print(f'\n{m[0]} peso: {m[1]}Kg. Peso de', end=' ')
    for dado in cadastro:
        if dado[0] == m[1]:
            print(f'[{dado[1]}]', end=' ')
print()