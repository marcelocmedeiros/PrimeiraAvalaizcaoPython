#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 02

'''
7- Faça um programa que calcule a área total (m2) de uma casa com 4 cômodos.
O usuário deve inserir a largura e comprimento de cada um dos cômodos,
calcular a área individual de cada um e por fim exibir a área total da casa.
'''

l1 = float(input('Largura do 1º comodo? '))
c1 = float(input('comprimento do 1º comodo? '))
a1 = l1 * c1
l2 = float(input('Largura do 2º comodo? '))
c2 = float(input('comprimento do 2º comodo? '))
a2 = l2 * c2
l3 = float(input('Largura do 3º comodo? '))
c3 = float(input('comprimento do 3º comodo? '))
a3 = l3 * c3
l4 = float(input('Largura do 4º comodo? '))
c4 = float(input('comprimento do 4º comodo? '))
a4 = l4 * c4
atot = a1 + a2 + a3 + a4
print('-=' * 20)
print(f'Área total do 1º comodo é de {a1}m².')
print(f'Área total do 2º comodo é de {a2}m².')
print(f'Área total do 3º comodo é de {a3}m².')
print(f'Área total do 4º comodo é de {a4}m².')
print(f'Área total da casa é de {atot}m².')
print('-=' * 20)
