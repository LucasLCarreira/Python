# Exercício 090
# Programa que leia nome e média de um aluno, guardando também a situação em um dicionário
# No final, mostre o conteúdo da estrutura na tela
aluno = {}
aluno['Nome'] = str(input('Nome: ')).strip().title()
aluno['Média'] = float(input('Média: '))
media = aluno['Média']
if media >= 6:
    aluno['Situação'] = 'Aprovado'
elif media >= 3:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-=' * 26)
for k, v in aluno.items():
    print(f'{k}: {v}',end=' | ')
print()
print('-=' * 26)

