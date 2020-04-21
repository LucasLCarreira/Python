# Exercício Python 040
# LEIA DUAS NOTAS E CALCULE A MEDIA
# <5: REPROVADO; ENTRE 5 E 6.9: RECUPERACAO; >=7: APROVADO
a = float(input('Digite a nota 1: '))
b = float(input('Digite a nota 2: '))
m = (a + b) / 2
if m >= 7:
    print('Parabéns, sua média é {:.2f} e você está aprovado!'.format(m))
elif 5 <= m < 7:
    print('Sua média é {:.2f} e você está em recuperação!'.format(m))
else:
    print('Sua média é {:.2f} e você está reprovado!'.format(m))

