#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 04

'''
8- Faça um Programa que peça uma data no formato dd/mm/aaaa e
determine se a mesma é uma data válida.
'''
print('=' * 40)
print('{:=^40}'.format(" PROGRAMA DATA VÁLIDA "))
print('=' * 40, '\n')

# variável dia = dd, mês = mm, ano = aaaa
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

print(f'A data {dia}/{mes}/{ano}')
#valida = False

# Meses com 31 dias
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or \
        mes == 8 or mes == 10 or mes == 12):
    if (dia <= 31):
        valida = True
        print('Data válida')
    else:
        print('Inválida')
# Meses com 30 dias
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia <= 30):
        valida = True
        print('Data válida')
    else:
        print('Inválida')
elif mes == 2:
    # Testa se é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if (dia <= 29):
            valida = True
            print('Data válida')
        else:
            print('Inválida')
    elif (dia <= 28):
        valida = True
        print('Data válida')
    else:
        print('Inválida')


