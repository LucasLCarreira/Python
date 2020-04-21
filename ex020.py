# Exercício Python 020
# Sorteio da ordem de apresentação dos trabalhos do aluno
# Mostre a ordem
import random
a = (input('Aluno 1: '))
b = (input('Aluno 2: '))
c = (input('Aluno 3: '))
d = (input('Aluno 4: '))
alunos = [a,b,c,d]
ordem = random.sample(alunos,4)
random.shuffle(alunos)
print('A ordem dos alunos é: {}'.format(ordem))
print('A ordem dos alunos é: {}'.format(alunos))