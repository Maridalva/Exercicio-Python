#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA
# TEM "SILVA" NO NOME
nome=str(input('Digite seu nome por gentileza:')).strip()
print('Seu nome possui Silva? {}'.format("SILVA"in nome.upper()))