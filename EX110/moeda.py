def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def aumento(preco=0, taxa=0, formato=False):
    res = preco * (1 + taxa/100)
    return res if formato is False else moeda(res)


def reducao(preco=0, taxa=0, formato=False):
    res = preco * (1 - taxa/100)
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f' {moeda} {preco:7.2f}'.replace('.',',')


def resumo(preco=0, taxaUP=0, taxaDOWN=0):
    print(f'-' * 27)
    print(f'RESUMO DO VALOR'.center(27))
    print(f'-' * 27)
    print(f'Preço:\t\t\t{moeda(preco)}\n'
          f'Dobro:\t\t\t{dobro(preco, True)}\n'
          f'Metade:\t\t\t{metade(preco, True)}\n'
          f'{taxaUP}% de aumento:\t{aumento(preco, taxaUP, True)}\n'
          f'{taxaDOWN}% de redução:\t{reducao(preco, taxaDOWN, True)}')
    print(f'-' * 27)