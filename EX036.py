# Escreva um programa para aprovar o
# empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo
# será negado.

casa=float(input('qual é o valor da casa? R$'))
sal=float(input('Qual é o salário do comprador?R$'))
anos=int(input("Em quantos anos ele vai pagar?"))
prest=casa / (anos * 12)
minimo=sal * 30 / 100
print('Para pagar a casa  de R${:.2f} em {} anos , '.format(casa,anos),end='')
print('A prestação será de {:.2f}. '.format(prest))
if prest<=minimo:
    print('IMPRESTIMO CONCEDIDO!')
else:
    print('EMPRESTIMO NEGADO!')