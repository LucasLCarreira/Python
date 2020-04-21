# Exercício Python 019
# Sorteio de 4 alunos para um apagar a lousa.
# Leia o nome deles e escreva o escolhido
import random
a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
d = str(input('Aluno 4: '))
alunos = [a,b,c,d]
s = random.choice(alunos)
print('O aluno sorteado para apagar a lousa é: {}'.format(s))