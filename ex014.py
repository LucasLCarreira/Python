# Exercício Python 014:
# Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit.
c = float(input('Digite a temperatura em graus Celsius: '))
f = (9 * c + 160) / 5
print('A conversão da temperatura para graus Farenheit é: {:.2f}'.format(f))