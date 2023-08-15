#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
peso=float(input('Digite o peso (km):'))
alt=float(input('Digite a altura (em metros):'))
imc= peso / (alt*alt  )
print('O IMC dessa pessoa é de {:.1f} '.format(imc))#casa decimal ex:1f
if  imc < 18.5:
    print('ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
 print('SOBREPESO!')
elif 30 <= imc < 40:
    print('OBESIDADE!')
else:
    print('OBESIDADE MORBIDA')