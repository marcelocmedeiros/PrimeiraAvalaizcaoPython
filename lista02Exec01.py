#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 02

'''
1- Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75)
e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de
combustível o usuário obterá com esses valores.
'''

valor_gas = float(input('Qual o valor do combustível?R$ '))
num = float(input('Qual o valor que deseja abastecer?R$ '))
valor_tot = num / valor_gas
print('-=' * 35)
print(f'O valor abastecido foi R${num:.2f} e a quantidade de combustivél é {valor_tot:.2f}l.')
print('-=' * 35)
print('  OBRIGADO, VOLTE SEMPRE!  ')
