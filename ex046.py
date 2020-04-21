# Exercício Python 046
# Contagem regressiva para estouro dos fogos de artificio, de 0 até 10, com pausa de 1 seg entre eles
from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('FOGOS DE ARTIFÍCIO ESTOURARAM!')
