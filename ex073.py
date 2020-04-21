# Exercício Python 073
# Crie uma tupla com os 20 primeiros colocados do campeonato brasileiro. Mostre:
# A - Apenas os 5 primeiros colocados
# B - Apenas os últimos 4 colocados
# C - Uma lista com os times em ordem alfabética
# D - Em que posição está o time Chapecoense

tabela = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico','São Paulo',
          'Internacional','Corinthians','Fortaleza','Goiás','Bahia',
          'Vasco','Atlético-MG','Fluminense','Botafogo','Ceará',
          'Cruzeiro','CSA','Chapecoense','Avaí')
chapecoense = tabela.index('Chapecoense')
print('-'*23)
print(f'\033[1m{"TABELA BRASILEIRÃO 2019":^20}\033[m')
print('-'*23)
pos = 1
for libertadores in range(0,5):
    print(f'\033[1;34m{pos}º {tabela[libertadores]}\033[m')
    pos += 1
for intermediaria in range(5,16):
    print(f'\033[1;35m{pos}º {tabela[intermediaria]}\033[m')
    pos += 1
for rebaixados in range(16,20):
    print(f'\033[1;31m{pos}º {tabela[rebaixados]}\033[m')
    pos += 1
print('-'*23)
print(f'\033[1;34mLIBERTADORES')
print(f'\033[1;35mZONA INTERMEDIÁRIA')
print(f'\033[1;31mREBAIXADOS\033[m')
print('-'*23)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print(f'A Chapecoense está na {chapecoense}ª posição')
