#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 01

'''
5 - Receba do usuário o ano em que estamos, e o ano que ele nasceu,
e calcule sua idade. Despreze os meses.
'''

anoAtual = int(input('Informe em que ano estamos: '))
anoNasceu = int(input('Qual o ano que você nasceu: '))
idade = anoAtual - anoNasceu

print('A sua idade é', idade, 'anos')
