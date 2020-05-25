#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 02

'''
3-Faça um programa que calcule a média de consumo de combustível de um veículo.
O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km)
e quantos litros foram gastos no percurso.
'''

kminic = float(input('Qual a sua kilometragem atual, km? '))
kmfinal = float(input('Qual a sua nova kilometragem, km? '))
gasl = float(input('Quantos litros de combustivel foram gastos? '))
média = (kmfinal - kminic) / gasl
print('-=' * 50)
print(f'Você percorreu {(kmfinal - kminic):.2f}km com {gasl}l de combustível, portanto sua média de consumo foi {média:.2f}km/l.')
print('-=' * 50)
