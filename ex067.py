# Exercício Python 067
# Mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuário
# Programa interrompido quando N for negativo

while True:
    print('=-=' * 14)
    n = int(input('Você quer saber a tabuada de qual valor? '))
    if n < 0:
        break
    contador = 0
    while contador < 10:
        contador = contador + 1
        produto = n * contador
        print(f'{n} x {contador:2} = {produto}')
print('FIM!')