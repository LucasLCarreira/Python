# Exercício 101
# Programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se a pessoa tem voto negado, opcional ou obrigatório nas eleições

def voto(an):
    """
    Define se o voto do usuário será obrigatório, opcional ou proibido
    :param an: Ano de nascimento do usuário
    :return: sem retorno
    """
    from datetime import datetime
    idade = datetime.now().year - an
    if idade < 16:
        print('Não vota!')
    elif idade >= 18 and idade < 65:
        print('Voto obrigatório!')
    else:
        print('Voto opcional!')


an = int(input('Digite o ano de nascimento: '))
voto(an)

