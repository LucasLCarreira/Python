# Exercício Python 089
# Programa que leia nome e duas notas de varios alunos e guarde tudo em lista composta
# No final mostre o boletim contendo a media,
# e permita que o usuário possa mostras as notas de cada aluno individualmente
sala = []
aluno = []
situacao = ''
while True:
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    res = str(input('Adicionar aluno? [S/N] ')).strip().upper()
    while res not in 'SN':
        res = str(input('Adicionar aluno? [S/N] ')).strip().upper()
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    sala.append(aluno[:])
    if res in 'N':
        break
    aluno.clear()
print('=-=' * 15)
print(f'Nº    NOME      MÉDIA   SITUAÇÃO')
for s in range(0, len(sala)):
    media = (sala[s][1] + sala[s][2]) / 2
    if media >= 6:
        situacao = 'Aprovado'
    elif 3 <= media < 6:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'
    print(f'{s + 1:<6}{sala[s][0]:10}{media:<8.2f}{situacao}')
print('-' * 45)
while True:
    nota = int(input('Mostrar as notas de qual aluno?'
                     '\n(999 para interromper!)\n'))
    print('-' * 45)
    if nota == 999:
        break
    print(f'Aluno: {sala[nota - 1][0]}\n'
          f'Nota 1: {sala[nota - 1][1]}\n'
          f'Nota 2: {sala[nota - 1][2]}')
    print('-' * 45)
