#FAÇA UM PROGRAMA QUE LEIA TRES NUMEROS E MOSTRE
# QUAL É O MAIOR E QUAL É O MENOR.,

n1=int(input('Digite o primeiro numero:'))
n2= int(input('Digite o segundo numero:'))
n3= int(input('Digite o terceiro numero:'))

#if n1<n2 and n1<n3:
   # menor= n1
#if n2<n3 and n2<n1:
 #  menor=n2
#if n3<n1 and n2<n3:
 #   menor= n3
 #VERIFICANDO QUEM É O MENOR
menor =n1
if n2<n1 and n2<n3:
 menor=n2
if n3<n1 and n3<n2:
    menor= n3

#VERIFICANDO QUEM É O MAIOR:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
        maior = n3

print('O menor valor digitado foi {}'.format(menor))
print('O maior  valor digitado foi {}'.format(maior))