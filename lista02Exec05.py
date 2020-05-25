#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 02

'''
5- Faça um programa que calcule o valor a ser pago por uma dívida em atraso.
O usuário deve informar o valor original da dívida (ex. R$ 50,00),
a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).
'''

div = float(input('Qual valor da sua divida?R$ '))
mora = int(input('Quantos dias você está atrasado? '))
valor = div + mora * 0.25
print('-=' * 50)
print(f'O valor da sua divida era R${div:.2f}, você tinha {mora} dias de atraso, portanto o valor apagar é R${valor:.2f}.')
print('-=' * 50)