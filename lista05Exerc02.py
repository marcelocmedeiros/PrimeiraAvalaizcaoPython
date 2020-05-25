#MARCELO CAMPOS DE MEDEIROS
#ADS UNIFIP P1 2020
#LISTA 05

'''
2- Faça um programa que leia um nome de usuário e a sua senha e
não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações.
'''

# while True gera loop infinito enquanto for digitado senha e usuário igual
while True:
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    # condição ou parametro parar o loop
    if nome != senha:
        break
    else:
        print('Erro. A senha deve ser diferente do nome.')

print("Usuário: %s | Senha: %s" %(nome, senha))
