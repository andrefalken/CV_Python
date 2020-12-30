# Desafio 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

# Criando o input para receber o nome do(a) usuário(a)
# A função .strip() remove espaçoes em branco antes e depois do nome
nome = str(input('Qual é o seu nome completo? ')).strip()

# Verificando se há "SILVA" no nome
# A variável nome tem seus caracteres transformados em maiúsculo através da função .upper()
print('No seu nome possui o nome "SILVA"? ', ('SILVA' in nome.upper()))
