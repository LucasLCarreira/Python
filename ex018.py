# Exercício Python 018
# Leia um ângulo e mostre seno, cosseno e tangente
import math
a = int(input('Digite um ângulo: '))
cos = math.cos(math.radians(a))
sen = math.sin(math.radians(a))
tan = math.tan(math.radians(a))
print('Para o ângulo {} graus\nSeno é {:.2f}\nCosseno é {:.2f}\nTangente é {:.2f}'.format(a,sen,cos,tan))
