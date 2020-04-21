# Exercício Python 061
# Leia o primeiro termo e a razão de uma progressão aritmética
# Mostre os 10 primeiros termos dessa progressão (while)

num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão aritmética: '))
c = 0
res = 0
while c < 10:
    c = c + 1
    final = num + res
    res = res + razao
    print(final,end='·')
print('FIM')

# Professor
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
c = 0
while c < 10:
    print(termo,end='·')
    termo = termo + razao
    c = c + 1
print('FIM')