#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO
#CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO.CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

from math import hypot
co=float(input('Qual é o comprimento do cateto oposto:'))
ca=float(input('qual é o comprimento do cateto adjacente'))


hip =hypot(co,ca)

print('A hipotenusa vai medir {:.2f} '.format(hip))
