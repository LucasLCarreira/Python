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