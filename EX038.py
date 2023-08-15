# Escreva um programa que leia dois números inteiros e compare-os
# . mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
num1= int(input('Primeiro numero:'))
num2=int(input('segundo numero:'))
print('\033[1mANALISANDO NUMEROS...')
if num1 > num2:
    print(f'\033[1:31m O número {num1} é maior que {num2}.')
elif num2 > num1:
    print(f'\033[1:31mO número {num2} é maior que {num1}.')
else:
    print(f'\033[1:31mOs números {num1} e {num2} são iguais.')
