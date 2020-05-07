# Exercício 109
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser formatado ou não pela função moeda(),
# desenvolvida no desafio 108

from EX109 import moeda

p = float(input(f'Digite o preço: R$ '))
print(f'{"Metade:":8}{moeda.metade(p, True)}')
print(f'{"Dobro:":8}{moeda.dobro(p, True)}')
print(f'{"Aumento:":8}{moeda.aumento(p, 10, True)}')
print(f'{"Redução:":8}{moeda.reducao(p, 13, True)}')