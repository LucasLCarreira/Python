# Exercício Python 047
# Mostre todos números pares no intervalo de 1 a 50
for c in range(1,51):
    if c % 2 == 0:
        print(c,end=' ')

for c in range(2,51,2): # menos etapas de processamento, ocupa menos espaço
    print(c)
