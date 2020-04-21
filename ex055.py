# Exercício Python 055
# Leia o peso de 5 pessoas, mostre o maior e o menor

maior = 0
menor = 0
for p in range(1, 6):
    peso = int(input("Digite o peso:"))
    if p == 1: #com o contador na primeira posição, o maior e o menor são iguais
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = p
        if peso < menor:
            menor = p
print("O maior valor é:", maior)
print("O menor valor é:", menor)
