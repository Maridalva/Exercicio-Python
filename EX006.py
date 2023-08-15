#CRIE UM ALGORITMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO
# TRIPO E RAIZ QUADARADA:

n = int(input('Digite um número: '))
d= n*2
t= n*3
r= n**(1/2)
print('O  dobro de: {}  vale  {}:'.format(n,d ))
print('O triplo de  {}  vale {}.\nA sua raiz quadrada de {} é igual á {}: '.format( n,t,n,r,n))
#OU PODE SER USADO ESTA VERSÃOprint('O seu dobro é: {}  o seu triplo é:  {} e sua raiz quadrada é {}'.format( n*2, n*3,n**2(1/2))
# PARA IDENTIFICAR A POTENCIA TAMBÉM , POSSO COLOCAR pow(n,(1/2)