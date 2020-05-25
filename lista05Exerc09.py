#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 05

'''
9- Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''

n = 0
while n < 50:
    n += 1
    if n % 2 != 0:
        print(n, end=', ')