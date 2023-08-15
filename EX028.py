#ESCREVA  UM PROGRMA QUE FAÇA  O COMPUTADOR "PENSAR"
# EM UM NUMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O
# USUÁRIO TENTAR DESCOBRIR  QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.

# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.

from random import randint
from time import sleep
computador=randint (0,5)# FAZ O COMPUTADOR PENSAR!!
print('--=--'*20)
print('vou pensar em um numero entre 0 e 5,tente advinhar!!')
print('--=--'*20)
jogador =int(input('Em que numero eu pensei?'))# jogador tenta advinhar
print('PROCESSANDO.....')
sleep(3)
if jogador ==computador:
    print('PARABENS!Você conseguiu me vencer!')
else:
    print('GANHEI!Eu pensei no número {} e nâo no numero {}.'.format(computador,jogador))
