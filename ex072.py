# Exercício Python 072
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem de zero a vinte (extenso)
# Seu programa deverá ler um número pelo teclado (0-20) e mostrá-lo por extenso

contagem = ('zero','um','dois','três','quatro','cinco','seis','sete',
            'oito','nove','dez','onze','doze','treze','quatorze','quinze',
            'dezesseis','dezessete','dezoito','dezenove','vinte')
print('Digite um número de 0 a 10!')
res = "S"
while res == 'S':
    c = int(input('Digite um número: '))
    if 0 <= c <= 20:
        print(f'Você digitou o número {contagem[c]}!')
        res = str(input('Quer continuar? [S/N] ')).strip().upper()
    else:
        print(f'Você digitou um número inválido!')
        res = str(input('Quer continuar? [S/N] ')).strip().upper()

    if res not in 'S':
        break
print('FIM!')


