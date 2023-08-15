#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM,
#MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO .
#A MULTA VAI CUSTAR 7,00 POR CADA KM ACIMA DO LIMITE .
vel = float(input('Quantos km por hora estava o carro? '))
if vel <= 80:
    print('Parabéns ! você está dentro do limite de velocidade! ')
else:
    print('Você ultrapassou o limite de 80 km/hora e foi multado!')
multa=(vel - 80)*7
if multa > 0:
    print('O valor da multa é de R$ {:.2f}'.format(multa))