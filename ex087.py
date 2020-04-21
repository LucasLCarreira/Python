# Exercício Python 087
# Aprimore o desafio anterior, mostrando:
# A - A soma de todos os valores pares
# B - A soma dos valores da terceira coluna
# C - O maior valor da segunda linha
linha = []
matriz = []
pares = soma = maior = 0
for l in range(1,4):
    for c in range(1,4):
        linha.append(int(input(f'Linha {l:^3}| Coluna {c:^3}: ')))
    matriz.append(linha[:])
    linha.clear()
print(f'\n{" MATRIZ ":-^24}')
print(' _____  ' * 3)
for l in range(0,3):
    for c in range(0,3):
        print(f'|{matriz[l][c]:^5}|',end=' ')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]
    print('\n|_____| |_____| |_____|')
print(f'\nA soma dos números pares é {pares}.')
print(f'A soma dos números da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {maior}.')
