# Desafio 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

# Criando o input para receber o nome do(a) usuário(a)
nome = input('Qual é o seu nome completo? ')

# Verificando se há "Silva" no nome
print('No seu nome possui o nome "Silva"? ', nome.find('Silva'))
