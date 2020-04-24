# Exercício 094
# Programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada um em um dicionario
# E todos os dicionários em uma lista. No final, mostre:
# A - Quantas pessoas foram cadastradas
# B - A média de idade
# C - Uma lista com todas as mulheres
# D - Uma lista com todas as pessoas com idade acima da média
cadastro = {}
lista = []
mulheres = []
acima = []
somaidade = 0
while True:
    cadastro['nome'] = str(input('Nome: ')).strip().title()
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    cadastro['idade'] = int(input('Idade: '))
    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro['nome'])
    lista.append(cadastro.copy())
    somaidade += cadastro['idade']
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print('=-=' * 10)
    if res == 'N':
        break
media = somaidade / len(lista)
print(f'Quantidade de cadastros:\n'
      f'{len(lista)}\n'
      f'A média de idade:\n'
      f'{media:.2f} anos\n'
      f'Mulheres cadastradas:')
for m in mulheres:
    print(m)
print(f'Pessas acima da média de idade:')
for a in range(0, len(lista)):
    if lista[a]['idade'] > media:
        print(lista[a]['nome'])



