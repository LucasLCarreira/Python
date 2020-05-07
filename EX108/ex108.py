# Exercício 108
# Adapte o desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado.

from EX108 import moeda

p = float(input(f'Digite o preço: R$ '))
print(f'{"Metade:":8}{moeda.moeda(moeda.metade(p))}')
print(f'{"Dobro:":8}{moeda.moeda(moeda.dobro(p))}')
print(f'{"Aumento:":8}{moeda.moeda(moeda.aumento(p, 10))}')
print(f'{"Redução:":8}{moeda.moeda(moeda.reducao(p, 13))}')