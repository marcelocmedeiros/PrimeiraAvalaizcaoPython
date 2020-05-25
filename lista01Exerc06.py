#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 01

'''
6 - Escreva um programa que leia uma temperatura em graus Fahrenheit,
transforme-a em graus Celsius e exiba o resultado.
'''

f = float(input('Qual a temperatura em Fahrenheit? '))
c = (f - 32) * 5/9
print('-=' * 35)
print(f'Sua temperatura em fahreinheit é {f}ºF, convertida para celsius é {c:.2f}ºC.')
print('-=' * 35)