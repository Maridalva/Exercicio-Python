#CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO
# E MOSTRE NA TELA SE ELE E PAR OU IMPAR.
num=int(input('DIGITE UM NUMERO:'))
resul=num % 2
if resul==0:
 print("O numero è {} PAR!!".format(num))
else:
    print('numero è {} impar!'.format(num))