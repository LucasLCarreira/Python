# Exercício Python 026
# Leia uma frase e mostre: quantos 'A', em que posição ela aparece pela primeira vez e última vez
frase = str(input('Digite uma frase: ')).strip()
minuscula = frase.lower()
print('Quantas vezes aparece a letra (a):',minuscula.count('a'))
print('Primeira posição:',minuscula.find('a')+1)
print('Última posição:',minuscula.rfind('a')+1)

# deixando a frase minuscula no input
frase2 = str(input('Digite uma frase: ')).lower().strip()
print('Quantas vezes aparece a letra A: {}'.format(frase2.count('a')))
print('Primeira posição: {}'.format(frase2.find('a')+1)) #+1 para não iniciar do 0
print('Última posição: {}'.format(frase2.rfind('a')+1))