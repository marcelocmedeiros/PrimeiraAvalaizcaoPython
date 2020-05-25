#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 01

'''
1 - Escreva um programa que converte valores de polegadas em centímetros
utilizando a seguinte fórmula: 1 polegada = 2,54cm;
'''

p = float(input('Quantas polegadas? '))
cm = p * 2.54
print('-=' * 35)
print(f'Quando {p} polegadas convertidas para centimetros teremos: {cm:.2f}cm.')
print('-=' * 35)