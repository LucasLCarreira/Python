# Exercício Python 025
# Leia o nome de uma pessoa e diga se tem 'Silva'
nome = input('Digite o nome de uma pessoa: ').strip()
minusculo = nome.lower()
print('silva'in minusculo)
print('silva'in nome.lower())