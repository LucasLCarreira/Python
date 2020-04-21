# Exercício Python 034
# Pergunte o salário do funcionario
# Salários > 1250, aumento de 10%
# Salários <= 1250, aumento de 15%

s = int(input('Digite o salário do funcionário: '))
if s > 1250:
    sr = s * (1 + 0.1)
    print('O salário reajustado é R$ {:.2f}'.format(sr))
else:
    sr = s * (1 + 0.15)
    print('O salário reajustado é R$ {:.2f}'.format(sr))