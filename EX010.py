#CRIE UM PROGRAMA QUEL LEIA QUANTO DINHEIRO UMA PESSOA  TEM NA CARTEIRA
# E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR:

#  CONSIDERE :US$ 1,00 = R$ 4.81

real= float(input("Quanto dinheiro você tem na carteira? \nR$"))
dolar = real/4.81
print('Com R${:.2f},você poderá comprar U$${:.2f}.'.format(real,dolar))

