# Exercício 112
# Dentro do pacote utilidades, no módulo dado, crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função input()
# mas com uma validação de dados para aceitar apenas valores monetarios

from EX112 import moeda
from EX112 import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 80, 35)