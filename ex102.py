# Exercício 102
# Programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial (fazer a docstring)
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            if c == 1:
                print(f'{c} =', end=' ')
            else:
                print(f'{c} x', end=' ')
    print(f)


n = int(input('Digite um número: '))
fatorial(n)
