# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO
# E MOSTRE SEU NOVO PREÇO.COM 5% DE DESCONTOS:

preço=float(input('qual é o valor do produto? R$'))
novo = preço - (preço * 5/100)
print('O produto que custava R${:.2f}, na promoção de 5%  custará R${:.2f}'.format(preço,novo))

