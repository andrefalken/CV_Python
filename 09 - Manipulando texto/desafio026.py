# Desafio 026
# Faça um programa que leia uma frase pelo teclado e mostre:

# Solicitando ao(a) usuário(a) que digite a frase
frase = input('Digite a frase: ')

# Quantas vezes aparece a letra a minúscula
print('A letra a minúscula aparece ', frase.count('a'), 'vezes na frase: {}'.format(frase))

# Em que posição a letra a aparece pela primeira vez
print('A letra a minúscula aparece a primeira vez no índice ', frase.find('a'), 'na frase: {}'.format(frase))

# Em que posição ela aparecer pela última vez