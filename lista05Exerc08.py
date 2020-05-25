#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 05

'''
8- Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

soma = 0
n = 1

while n <= 5:
    num = int(input(f'Informe o {n}° número: '))
    n += 1
    soma += num
    media = soma / 5

print('A soma dos números é %i e sua média é %.2f' %(soma, media))

