#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 03

'''
10 - Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!"
 ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

# variáveis
turno = str(input('Em que turno você estuda, digite "M" matutino ou "V" Vespertino ou "N" Noturno? ')).strip().upper()

# condicional para informar o turno e retornar mensagem
if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
