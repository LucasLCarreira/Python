# Exercício Python 079
# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista, ele não será adicionado
# Exiba todos os valores únicos, em ordem crescente.
lista = []
while True:
    num = (int(input('Digite um número: ')))
    if num in lista:
        print(f'O valor {num} já foi adicionado anteriormente.',end=' ')
    else:
        lista.append(num)
    res = str(input('Quer adicionar mais um? [S/N] ')).strip().upper()
    while res not in 'SN':
        res = str(input('Quer adicionar mais um? [S/N] ')).strip().upper()
    if res == 'N':
        break
lista.sort()
print(lista)
