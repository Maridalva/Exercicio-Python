#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE :
#=>O NOME COM TODAS AS LETRAS MAIUSCULA EM MINUSCULAS.
#=> QUANTAS LETRAS AO TODO (SEM CONNSIDERAR OS ESPAÇOS).
#=>QUANTAS LETRAS TEM O PRIMERO NOME.

nome=str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome....')
print('Seu nome em maisculo é {}.' .format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))
separa=nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.find('')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0],len(separa[0])))
