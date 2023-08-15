#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
atual=date.today().year
ano=int(input('Digite o ano de nascimento do atleta:'))
idade= atual -ano
print('O atleta tem {} anos.'.format(idade))
if idade <=9:
    print('Com o ano  {} se enquadra na categoria MIRIM!'.format(ano))
elif idade <=14:
    print(' Com  o ano {} se enquadra na categoria INFANTIL!'.format(ano))
elif idade <=19:
    print('Com o ano {}  se enquadra na categoria JUNIOR!'.format(ano))
elif idade <=25 :
     print('Com o ano {} se enquadra na categoria SÊNIOR !'.format(ano))
else:
    print('Com o ano se enquadra na Categoria MASTER!'.format(ano ))