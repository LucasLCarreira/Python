# Exercício 092
# Programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionáro.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input('Nome: ')).strip().title()
ano = int(input('Ano de nascimento: '))
idade = datetime.today().year - ano
cadastro['Idade'] = idade
cadastro['CTPS'] = int(input('CTPS [Digite 0, caso não possua]: '))

if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] + 35) - ano

for k, v in cadastro.items():
    print(f'{k}: {v}')

