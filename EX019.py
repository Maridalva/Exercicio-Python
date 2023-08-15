#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.FAÇA UM PROGRAMA QUE AJUDE ELE ,
# LENDO O NOME DELES E ESCREVA O NOME DO ESCOLHIDO.
import random#randomizador de elementos uma escolha  dentro dos elemntos o computador escolhe
N1=str(input('Primeiro aluno:'))
N2=str(input('Segundo aluno:'))
N3=str(input('Terceiro aluno:'))
N4=str(input('Quarto aluno:'))
lista=(N1,N2,N3,N4)
escolhido= random.choice(lista)

print('O aluno escolhido foi {} '.format(escolhido))
