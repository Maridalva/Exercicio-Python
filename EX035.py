#   DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRES RETAS
#   E DIGA AO USUARIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO .
print('-='*20)
print('Analisador de triangulos:')
print('-='*20)
R1=float(input('Primeiro seguimento:'))
R2=float(input('Segundo seguimento:'))
R3=float(input('Terceiro seguimento:'))
if R1< R2 + R3 and R2 < R1 + R3 and R3 < R1 +R2:
    print('Os segmentos acima PODEM FORMAR TRIANGULOS!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIANGULOS !')