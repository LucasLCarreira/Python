# Exercício 105
# Programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# - quantidade de notas
# - a maior nota
# - a menor nota
# - a média da turma
# - a situação (opcional)
# Adicione também as docstrings da função

def notas(*nota, situacao=False):
    turma = {}
    lista = []
    c = 1
    total = 0
    for n in nota:
        lista.append(n)
        total += n
    media = total / len(lista)
    if media >= 7:
        resultado = 'Aprovado'
    elif media >= 5:
        resultado = 'Recuperação'
    else:
        resultado = 'Reprovado'
    turma['Total de notas'] = len(lista)
    turma['Maior nota'] = sorted(lista)[len(lista) - 1]
    turma['Menor nota'] = sorted(lista)[0]
    turma['Média'] = media
    if situacao == True:
        turma['Situação'] = resultado
    for k, v in turma.items():
        print(f'{k}: {v}')


notas(5, 7, 8, 4, situacao=True)
notas(5, 8, 2, 3, 0, situacao=False)
