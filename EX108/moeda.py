def metade(preco):
    res = preco / 2
    return res

def dobro(preco):
    res = preco * 2
    return res


def aumento(preco, taxa):
    res = preco * (1 + (taxa / 100))
    return res


def reducao(preco, taxa):
    res = preco * (1 - (taxa / 100))
    return res


def moeda(preco=0, moeda='R$'):
    return f' {moeda} {preco:7.2f}'.replace('.',',')