#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 05

'''
7- Faça um programa que leia 5 números e informe o maior número.
'''
# por For

maior = 0
n = 1

while n <= 5:
    num = int(input(f'Informe o {n}° número: '))
    n += 1

    if num > maior:
        maior = num

print('O maior número é %.i' % maior)
