# Exercício Python 086
# Programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado
# Mostre a matriz na tela com a formatação correta
linha = []
matriz = []
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
    print('\n|_____| |_____| |_____|')

# https://www.youtube.com/watch?v=EGmlFdwD4C4&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=18
# Resolução do professor
print()
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
