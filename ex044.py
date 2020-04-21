# Exercício Python 044
# CALCULE O VALOR A SER PAGO POR UM PRODUTO
# CONSIDERANDO PRECO NORMAL E CONDICAO DE PAGAMENTO
# A VISTA DINHEIRO OU CHEQUE: 10% DE DESCONTO
# A VISTA NO CARTAO: 5% DE DESCONTO
# ATÉ 2 X NO CARTAO: PRECO NORMAL
# 3X OU MAIS NO CARTAO: 20% DE JUROS
p = float(input('Digite o preço do produto:\n'))
c = int(input('Digite a forma de pagamento:'
              '\n[0] À vista em dinheiro ou cheque'
              '\n[1] À vista no cartão'
              '\n[2] Em 2x no cartão'
              '\n[3] Em 3x ou mais no cartão\n'))
if c == 0:
    v = p * (1 - 0.1)
    print('O valor a ser pago é R$ {:.2f}'.format(v))
elif c == 1:
    v = p * (1 - 0.05)
    print('O valor a ser pago é R$ {:.2f}'.format(v))
elif c == 2:
    v = p
    print('O valor a ser pago é R$ {:.2f}'.format(v))
elif c == 3:
    v = p * (1 + 0.2)
    print('O valor a ser pago é R$ {:.2f}'.format(v))
