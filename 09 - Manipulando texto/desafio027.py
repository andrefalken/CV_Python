# Desafio 027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Pedindo ao(a) usuário(a) que entre com seu nome completo
nome_completo = input('Digite seu nome completo: ').strip()

# Fazendo a separação do nome
nome_separado = nome_completo.split()
primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[-1]
print('O seu primeiro nome é {} e o seu último nome é {}.'.format(primeiro_nome, ultimo_nome))
