# Exercício 098
# Programa que tenho uma função CONTADOR() que receba 3 parâmetros: início, fim e passo
# A - de 1 a 10, passo 1
# B - de 10 a 0, passo 2
# C - contagem personalizada (usuário determina parâmetros)

def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if f > i:
        print('-=' * 20)
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f + 1, p):
            print(c, end=' ')
        print()
    elif f < i:
        print('-=' * 20)
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f - 1, -p):
            print(c, end=' ')
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
