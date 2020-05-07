# Exercício 110
# Adicione ao módulo moeda.py criano uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que
# já temos no módulo criado

from EX110 import moeda

p = float(input(f'Digite o preço: R$ '))
moeda.resumo(p, 80, 35)