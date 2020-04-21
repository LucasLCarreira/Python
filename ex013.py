# Exercício Python 013:
# Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento.
s = float(input('Digite o salário atual: R$ '))
print('O salário reajustado é R$ {:.2f}'.format(s*(1+(15/100))))
