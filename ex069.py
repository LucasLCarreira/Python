# Exercício Python 069
# Leia a idade e o sexo de várias pessoas
# A cada pessoa, perguntar se quer continuar cadastrando
# Mostre: quantas pessoas > 18; Quantos homens; quantas mulheres < 20
pessoa = 1
maiores18 = homem = 0
mulherMenos20 = 0
while True:
    print('·' * 32)
    print(f'{pessoa}ª pessoa:')
    idade = int(input('Qual é a idade? '))
    sexo = str(input('Qual é o sexo? [M/F] ')).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Qual é o sexo? [M/F] ')).strip().upper()[0]
    res = str(input('Continuar cadastrando? [S/N] ')).strip().upper()[0]
    while res not in 'SsNn':
        res = str(input('Continuar cadastrando? [S/N] ')).strip().upper()[0]
    pessoa += 1
    if idade >= 18:
        maiores18 += 1
    if sexo == 'M':
        homem += 1
    else:
        if idade < 20:
            mulherMenos20 += 1
    if res in 'Nn':
        break
print('·' * 32)
print('FIM')
print(f'Foram cadastradas {maiores18} pessoas menores de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {mulherMenos20} mulheres com menos de 20 anos.')