# Exercício 097
# Programa que tenha uma função chamada escreva() que receba um texto qualquer como parâmetro
# mostre uma mensagem com tamanho adaptável

def escreva(texto):
    print('~' * (len(texto) + 4))
    print(f'  {texto}')
    print('~' * (len(texto) + 4))


texto = str(input('Digite um texto: '))
escreva(texto)