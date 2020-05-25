#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 05

'''
3-Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

# gera loop infinito enquanto não for digitado nome > 3 digitos
while True:
    nome = input('Digite seu nome: ')
    if len(nome) > 3:
        break
    else:
        print('Digite novamente.')

# gera loop infinito enquanto caso idade seja >0 ou <150
while True:
    idade = int(input('Digite sua idade: '))
    if idade > 0 and idade <= 150:
        break
    else:
        print('Digite novamente.')

# gera loop infinito enquanto não dgitar salário > 0
while True:
    salario = float(input('Digite seu salário: '))
    if salario >= 0:
        break
    else:
        print('Digite novamente.')

# gera loop infinito enquanto não for dgitado F ou M
while True:
    sexo = input('Digite seu sexo(F-feminino ou M-masculino): ').upper()
    if sexo in 'FM':
        break
    else:
        print('Digite novamente.')

# gera loop infinito enquanto não for dgitado Estado Civil: 's', 'c', 'v', 'd';
while True:
    estado = input('Digite seu estado civil(S-solteito, C-casado, V-Viúvo, D-divorciado): ').upper()
    if estado in 'SCVD':
        break
    else:
        print('Digite novamente.')
