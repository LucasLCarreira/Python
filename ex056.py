# Exercício Python 056
# Leia nome, idade e sexo de quatro pessoas. Mostre:
# média de idade, qual é o nome do homem mais velho, quantas mulheres tem menos de 20 anos
maisvelho = ''
maior = 0
somaIdade = 0
somaMulheres = 0
for c in range(0,4):
    nome = str(input('Nome: ')).strip
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F) ou (M): ')).upper().strip
    somaIdade = somaIdade + idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
            maisvelho = nome
    if sexo == 'F':
        if idade < 20:
            somaMulheres = somaMulheres +1
print('A média de idade é {:.2f}.'.format(somaIdade / 4))
print('O homem mais velho é o {}.'.format(maisvelho))
print('Existe(m) {} mulher(es) com menos de 20 anos.'.format(somaMulheres))