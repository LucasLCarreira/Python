# Exercício Python 036
# PROGRAMA PARA FINANCIAMENTO IMOBILIARIO
# LEIA VALOR DA CASA, SALARIO DO COMPRADOR E EM QUANTOS ANOS VAI PAGAR
# CALCULE VALOR DA PRESTACAO, SABENDO QUE NAO PODE EXCEDER 30% DO SALARIO]
# SE EXCEDER: EMPRESTIMO NEGADO

i = float(input('Qual é o valor do imóvel? R$ '))
s = float(input('Qual é o salário do comprador? R$ '))
a = int(input('Quantos anos de financiamento? '))
p = i / (a * 12)
if p <= (s * 0.3):
    print('\033[1;34mParabéns! Financiamento aprovado! Sua prestação será de R$ {:.2f}!\033[m'.format(p))
else:
    print('\033[1;31mInfelizmente seu financiamento foi negado! '
          'A prestação de R$ {:.2f} ultrapassa o limite de 30% do seu salário!\033[m'.format(p))

