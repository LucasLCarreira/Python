# Crie um código em Python que teste se o site Pudim está acessivel

import urllib
import urllib.request

try:
    site = urllib.request.urlopen(('http://www.pudim.com.br'))
except:
    print('O site não está acessível!')
else:
    print('O site está acessível!')