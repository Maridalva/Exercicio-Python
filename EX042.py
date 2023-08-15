# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
print('===='*30)
print('VERIFICANDO O TRIANGULO..... ')
print('==='*30)

r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and r1 > r2 - r3 and r2 > r1 - r3 and r3 > r2 - r1:
    if (r1 == r2 and r1 == r3 and r2 == r3):
        print(" EQUILÁTERO")
    elif (r1 != r2 and r1 != r3 and r2 != r3):
        print("ESCALENO")
    else:
        print("ISOSCELES")
else:
    print("Não é possível formar um triangulo!")