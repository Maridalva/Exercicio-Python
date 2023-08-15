#CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER
# PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA

#ex digite um numero: 6.127
#o numero 6.127 tem a parte inteira 6.
import math
num=float(input('Digite um numero:'))

print('O valor digitado foi de {} e sua porçâo inteira è de {}.'.format(num,int(num)))