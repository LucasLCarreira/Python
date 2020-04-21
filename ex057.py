# Exercício Python 057
# Leia o sexo, mas só aceite 'm' ou 'f'
# Caso esteja errado, peça a digitação novamente
sexo = str(input('Qual é o sexo? [M/F] ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    print('Digite o parâmetro corretamente!')
    sexo = str(input('Qual é o sexo? [M/F] ')).upper().strip()[0]
print('FIM')

# while sexo not in 'MF': outra forma
