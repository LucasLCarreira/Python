# Exercício Python 053
# Leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
frase = str(input('Digite uma frase: ')).strip().upper()
c = -1
dividido = frase.split()
unido = ''.join(dividido)
comprimento = (len(unido))
for a in range(comprimento):
    print(unido[comprimento + c],end='')
    c = c - 1

# Resolução do professor
Frase = str(input('\nDigite uma frase: ')).strip().upper()
palavras = Frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(inverso)
if inverso == junto:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')