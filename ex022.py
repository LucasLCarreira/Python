# Exercício Python 022
# Leia o nome completo: letras maiusculas, minusculas, quantas letras sem espaços, quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo: ')).strip() # elimina os espaços antes e depois da string
print(nome.upper())
print(nome.lower())
print((len(nome))-(nome.count(' ')))
dividido = nome.split()
print(len(dividido[0]))
# Outra maneira de identificar quantas letras tem o primeiro nome
print(nome.find(' '))
# Ao localizar o primeiro espaço, encontra-se a primeira posição posterior a última letra do 1º nome