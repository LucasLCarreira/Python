# Exercício Python 029
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h, mostre que foi multado
# A multa custa R$ 7,00 para cada km acima do limite.

v = int(input('O radar detectou a velocidade: '))
if v > 80:
    m = (v - 80) * 7
    print('O carro foi multado, devido à velocidade de {}km/h, e irá pagar uma multa de {} reais.'.format(v,m))

