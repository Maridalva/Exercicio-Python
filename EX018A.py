#FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O
# VALOR DO SENO , COSSENO E TANGENTE DESSE ANGULO.
from math import radians,sin,cos, tan
ang=float(input('Digite o angulo que deseja:'))

seno=sin(radians(ang))
print('O angulo de {} tem SENO de {:.2f}.'.format(ang,seno))

cosseno= cos(radians(ang))
print('O angulo de {} tem COSSENO de {:.2f}.'.format(ang,cosseno))

tangente= tan(radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}.'.format(ang,tangente))