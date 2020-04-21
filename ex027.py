# Exercício Python 027
# Leia nome completo, mostrando o primeiro e o último separadamente
nome = str(input('Digite o nome completo:')).strip()
dividido = nome.split()
print('Primeiro nome:',dividido[0])
print('Último nome:',dividido[len(dividido)-1])
