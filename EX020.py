# O mesmo professor  do desafio anterior quer sortear a ordem
# de trabalhos dos alunos . faça um programa que leia
# o nome dos quatro  alunos e mostre a ordem sorteada.
import random# aleatorio
A1=str(input('digite o primeiro aluno:'))
A2=str(input('digite o segundo aluno:'))
A3=str(input('digite o terceiro aluno:'))
A4=str(input('digite o quarto aluno:'))
lista=[A1,A2,A3,A4]
random.shuffle(lista)
print("A ordem de apresentação será .")
print(lista)
