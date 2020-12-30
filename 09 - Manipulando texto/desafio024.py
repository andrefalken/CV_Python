# Desafio 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

# Criando um input para receber o nome da cidade
# A função strip elimida os espaços antes e depois do que o usuário digita
cidade = str(input('Qual é o nome da sua cidade natal? ')).strip()


# Aqui verificamos se do índice 0 ao índice 4 há o nome 'SANTO'
# Para evitar falhas, colocamos o texto que o usuário digitar em maiúsculo com a função .upper()
print('Na sua cidade natal possui o nome "SANTO"? ', cidade[:5].upper() == 'SANTO')
