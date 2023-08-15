#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA
# DE UMA VIAGEM EM KM . CALCULE O PREÇO DA PASSAGEM .
# COBRANDO R$0,50 POR KM PARA VIAGENS
# ATE 200KM E R$0,45 PARA VIAGENS LONGAS.
dist= float(input('Qual é a distancia da viagem ? '))
print("Você esta prestes a começar uma viagem de {} km".format(dist))

if dist <= 200:
    preço= dist* 0.50
#preço= ditancia *0.50 if distancia <=200 else distancia *0.45
# pode ser usado desta maneira tbm mais simplificada.

else:
 preço=dist* 0.45
 print('O preço da sua passagem será de R$ {:.2f}'.format(preço))