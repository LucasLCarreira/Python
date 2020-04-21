# Exercício Python 004:
# Faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e
# todas as informações possíveis sobre ele.

a = (input('Digite algo: '))
print('O tipo primitivo deste valor é {}'.format(type(a)))
print('É alfabético?',a.isalpha())
print('É numérico?',a.isnumeric())
print('É alfanumérico?',a.isalnum())
print('Só tem espaços?',a.isspace())
print('Está em caixa alta?',a.isupper())
print('Está em caixa baixa?',a.islower())
print('Está capitalizada?',a.istitle())

