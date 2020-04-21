# Exercício Python 024
# Leia o nome de uma cidade. Começa com 'SANTO'
cidade = str(input('Digite o nome de uma cidade: ')).strip()
minusculo = cidade.lower()
santo = 'santo'in minusculo[0:5]
print(santo)
# outra forma
print(cidade[:5].lower() == 'santo')
