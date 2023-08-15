#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('LOJA DA MARI'))

valor= float(input('Qual é o valor das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ]  á VISTA DINHEIRO/CHEQUE 
[ 2 ]  á VISTA NO CARTÃO
[ 3 ]  2X NO CARTÃO 
[ 4 ]  3X OU MAIS NO CARTÃO ''')
opção=int(input('Qual é a opção?'))

if opção ==1:
    total =valor-(valor * 10/100)

elif opção ==2:
    total= valor-(valor * 5/100)

elif opção==3:
    total= valor
    parcela = total/2
    print('Sua compra será parcelada 2x vezes de R${:.2f} SEM JUROS'.format(parcela))

elif opção == 4:
 total= valor + ( valor *20 /100)
totalparc =int(input('Quantas Parcelas?'))
parcela = total /totalparc
print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS.'.format(totalparc,parcela))
print('Sua compra de R$ {:.2f } vai custar R$ {:.2f} no final! '.format(valor, total))