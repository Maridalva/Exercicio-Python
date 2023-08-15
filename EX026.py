#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE NO FINAL :
# QUANTAS VEZES PARECE A LETRA "A"
# EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ.
frase=str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece quantas vezes? {} '.format(frase.count('A')))
print('A posição em que ela aparece a primeira vez? {}'.format(frase.find('A')+1))
print('A posição em que ela aparece a última vez? {}'.format(frase.rfind('A')+1))
print('A frase contem quantas letras e espaços? {}'.format(len(frase)-frase.count(' ')))