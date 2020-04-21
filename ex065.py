# Exercício Python 065
# Leia vários números inteiros
# Mostre a média, o maior e o menor
# Deve perguntar se o usuário quer continuar a digitar
menor = 0
maior = 0
res = 'S'
soma = 0
contador = 0
while res == 'S':
    n = int(input('Digite um número: '))
    res = str(input('Quer inserir mais um número: [S/N] ')).upper().strip()
    soma = soma + n
    contador = contador + 1
    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / contador
print('A média dos valores digitados é {}, o maior valor é {} e o menor valor é {}.'
      .format(media, maior, menor))
