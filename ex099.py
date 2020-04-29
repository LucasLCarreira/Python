# Exercício 099
# Programa que tenha a função MAIOR(), que receba vários parâmetros e diga qual é o maior

def maior(*numero):
    lista = numero
    ordem = sorted(lista)
    ultimo = ordem[len(sorted(ordem)) - 1]
    print('-=' * 30)
    print(f'Analisando os valores passados:\n'
          f'Os valores são:',end=' ')
    for l in lista:
      print(l,end=' ')
    print(f'\nTotal de valores: {len(lista)}.\n'
        f'O maior valor da lista é {ultimo}.')


maior(1, 4, 1, 8, 2, 6, 10, 2)
maior(4, 5, 7, 1, 9)

from time import sleep

# Resolução do professor

def maior(*num):
    print('-=-' * 20)
    for n in num:
        print(f'{n} ', end='')
    print(f'Ao todo foram digitados {len(num)} números.')
    maior_numero = 0
    for n in num:
        if n > maior_numero:
            maior_numero = n
    print(f'Sendo o maior deles o número {maior_numero}.')
    sleep(1)


maior(5, 6, 8, 1, 9, 2, 3, 0)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()