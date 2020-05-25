#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 02

'''
10- Faça um programa que calcula o novo valor do salário de um funcionário.
O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).
'''

sal = float(input('Qual o valor do seu salário? R$ '))
reaj = sal + (sal * 0.135)
print('-=' * 50)
print(f'O valor do seu salário era R${sal:.2f}, mas com reajuste de 13,5% seu novo sálario será de R${reaj:.2f}.')
print('-=' * 50)
