# Crie um programa que leia o nome completo de uma pessoa e mostre:
nomecompleto = input('Digite seu nome completo: ')

# O nome com todas as letras maiúcsulas
print('O seu nome com todas as letras maiúsculas:', nomecompleto.upper(),'.')

# O nome com todas as letras minúsculas
print('O seu nome com todas as letras minúsculas:', nomecompleto.lower(),'.')

# Quantas letras tem o seu nome (sem considerar os espaços em branco)
semespacos = nomecompleto.replace(" ","")
print('O seu nome sem espaços contém um total de', semespacos.__len__(), 'caracteres.')

# "Início de código errado"
# Quantas letras tem o primeiro nome
#nomedivido = nomecompleto.split()
#nomedivido2 = nomedivido(0)
#print('O primeiro nome possui um total de:', nomedivido2.__len__(), 'letras.')
# "Fim de código errado"

# Quantas letras tem o primeiro nome
nome_fatiado = nomecompleto.split()
primeiro_nome = nome_fatiado[0]
print('O primeiro nome possui um total de:', primeiro_nome.__len__(), 'letras.')
