#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA.
#MOSTRANDO EM SEGUIDA O PRIMEIRO NOME E O ULTIMO NOME SEPARADAMENTE.
#Ex ANA MARIA DE SOUZA
# PRIMEIRO= ANA
# ÚLTIMO= SOUZA

nome=str(input('Digite seu nome completo:')).strip()
nome= nome.split()
print("Prazer em te conhecer!")
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))