#FAÇA UM PROGARAM QUE LEIA UM NUMERO DE 0 A 999 E MOSTRE NA TELA CADA
# UM DOS DIGITOS SEPADOS.
#EX:DIGITE UM NUMERO: 1834
# UNIDADE :4      DEZENA: 3   CENTAVOS: 8 MILHAR :1

num=int(input('Digite um numero:'))
und = num//1 % 10
d=num // 10 % 10
c=num//100 % 10
m=num // 1000 % 10

print('Analisando o numero: {} '.format(num))
print('unidade : {}'.format(und))
print('dezena : {}'.format(d))
print('centena : {}'.format(c))
print('milhar: {}'.format(m))