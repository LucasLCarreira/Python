# Exercício Python 043
# LEIA O PESO E ALTURA DE UMA PESSOA, CALCULE IMC E MOSTRAR STATUS:
# ABAIXO DE 18.5: ABAIXO DO PESO
# ENTRE 18.5 E 25: PESO IDEAL
# 25 ATE 30: SOBREPESO
# 30 ATE 40: OBESIDADE
# ACIMA DE 40: OBESIDADE MÓRBIDA
p = float(input('Digite o peso (kg): '))
h = float(input('Digite a altura (cm): '))
imc = p / ((h/100)**2)
if imc < 18.5:
    print('O IMC é {:.2f} que corresponde a ABAIXO DO PESO'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('O IMC é {:.2f} que corresponde a PESO IDEAL'.format(imc))
elif imc >= 25 and imc < 30:
    print('O IMC é {:.2f} que corresponde a SOBREPESO'.format(imc))
elif imc >= 30 and imc < 40:
    print('O IMC é {:.2f} que corresponde a OBESIDADE'.format(imc))
else:
    print('O IMC é {:.2f} que corresponde a OBESIDADE MÓRBIDA'.format(imc))



