#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 05

'''
5- Altere o programa anterior permitindo ao usuário informar as populações e
as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

habitantesA = int(input('Informe a quantidade de habitantes da cidade A: '))
taxaA = float(input('Informe a taxas de crescimento da cidade A: '))
habitantesB = int(input('Informe a quantidade de habitantes da cidade B: '))
taxaB = float(input('Informe a taxas de crescimento da cidade B: '))

if habitantesA == habitantesB:
    print('As populações são iguais')

if habitantesA < habitantesB:
    if taxaA <= taxaB:
        print('Diante das taxas de crescimento não é possível que cidade A alcance a população da cidade B')
    else:
        anos = 0

        while habitantesA <= habitantesB:
            habitantesA = habitantesA + habitantesA * (taxaA / 100)
            habitantesB = habitantesB + habitantesB * (taxaB / 100)
            anos += 1
            print("Mantidas as taxas de crescimento de 'A' e 'B', 'A' levara %i anos para alcançar 'B'" % (anos))

if habitantesB < habitantesA:
    if taxaB <= taxaA:
        print('Diante das taxas de crescimento não é possível que cidade B alcance a população da cidade A')
    else:
        anos = 0

        while habitantesB <= habitantesA:
            habitantesA = habitantesA + habitantesA * (taxaA / 100)
            habitantesB = habitantesB + habitantesB * (taxaB / 100)
            anos += 1
            print("Mantidas as taxas de crescimento de A' e 'B', 'B' levara %i anos para alcançar 'A'" % (anos))


