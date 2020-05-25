#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 05

'''
1- Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
'''

# while True gera loop infinito enquanto não for digitado o valor dentro do parametro
while True:
    nota = float(input('Digite a nota: '))
    # condição ou parametro parar o loop
    if nota >= 0 and nota <= 10:
        break
    else:
        print('Nota inválida. Digite novamente')
