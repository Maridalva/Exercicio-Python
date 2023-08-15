# FAÇA UM ALGORITMO QUE LEIA O SÁLARIO  DE UM FUNCIONÁRIO
# E MOSTRE SEU NOVO SALÁRIO ,COM 15% DE AUMENTO:

sal=float(input('Qual é o salario do funcionario? R$'))
novo = sal + (sal * 15 /100)
print('O salario  que era de  R${:.2f}, com o aumento de 15% ,passará a ser de  R${:.2f}'.format(sal,novo))

