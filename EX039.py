#Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora exata de se alistar ou sejá passou do tempo do alistamento.
# Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

from datetime import date
Anoatual= date.today().year
nasc= int(input('Ano de nascimento:'))
idade= Anoatual - nasc
print('Quem nasceu em {} tem {} anos em {} .'.format(nasc, idade, Anoatual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo= 18 - idade
    print('Você ainda não tem 18 ANOS!Ainda falta {} anos para o ALISTAMENTO.'.format(saldo))
    ano=Anoatual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo= idade - 18
    print('Voce  deveria ter alistado ha {} ANOS!! '.format(saldo))
    ano= Anoatual-saldo
print('Seu alistamento foi em {} .'.format(ano))