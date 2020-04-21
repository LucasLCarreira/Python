# Exercício Python 077
# Crie um programa que tenha uma tupla com várias palavras
# Mostre quais são as vogais para cada palavra

tupla = ('Lucas', 'Lasevicius', 'Carreira', 'estuda', 'Análise', 'e', 'Desenvolvimento', 'de', 'Sistemas')
print('-'*30)
print('\033[1mVOGAIS DE CADA PALAVRA:\033[m')
print('-'*30)
for palavra in tupla:
    print(f'\n\033[1m{palavra}:\033[m', end=' ')
    for vogal in palavra:
        if vogal.lower() in 'aáâãàeéêiíoôóuûú':
            print(vogal, end=' ')


