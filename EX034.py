# ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONÁRIO
# E CALCULE O VALOR DE DE SEU AUMENTO.
#PRA SALARIO SUPERIORES A R$1.250,00 CALCULE UM AUMENTO DE 10%.
# PARA INFERIORES OU IGUAIS ,O AUMENTO É DE 15%.
salario= float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo= salario +(salario * 15 / 100)
else:
   novo= salario +( salario * 10 / 100)
   print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora  '.format(salario,novo))