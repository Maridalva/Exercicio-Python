#FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O
# VALOR DO SENO , COSSENO E TANGENTE DESSE ANGULO.
import math
ang=float(input('Digite o angulo que deseja:'))

seno=math.sin(math.radians(ang))
print('O angulo de {} tem SENO de {:.2f}.'.format(ang,seno))

cos=math.sin(math.radians(ang))
print('O angulo de {} tem COSSENO de {:.2f}.'.format(ang,cos))

tang= math.sin(math.radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}.'.format(ang,tang))
