#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
N1=float(input('digite a primeira nota:'))
N2 =float(input('Digite a segunda nota:'))
media =(N1+N2 )/2
print('De acordo com a nota {:.1f} e  {:.1f} a media atingida foi de {} !'.format(media,N1,N2))
if 7 > media >= 5:
    print(' ALUNO EM RECUPERAÇÃO!')
elif media < 5 :
    print(' ALUNO REPROVADO!')
elif media >=7 :
    print('ALUNO APROVADO!')