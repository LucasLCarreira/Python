# Exercício Python 062
# Melhore o desafio 61, perguntando se o usuário quer mostrar mais termos
# programa encerra quando usuário escolher 0 termos

num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão aritmética: '))
c = 0
soma = 0
while c < 10:
    c = c + 1
    res = num + soma
    soma = soma + razao
    print(res, end=' ')
q = 1
soma = razao
while q != 0:
    q = int(input('\nQuer inserir mais termos? '))
    c = 0
    while c < q:
        res = res + soma
        print(res, end=' ')
        c = c + 1
print('FIM')

# Professor
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
c = 0
total = 0
mais = 10 # Enunciado pede 10 primeiros termos
while mais != 0:
    total = total + mais
    while c < total:
        print(termo,end='·')
        termo = termo + razao
        c = c + 1
    mais = int(input('\nQuer mostrar mais quantos termos? '))
print('FIM!{} termos mostrados!'.format(total))