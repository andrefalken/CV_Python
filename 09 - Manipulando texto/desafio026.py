# Desafio 026
# Faça um programa que leia uma frase pelo teclado e mostre:

# Solicitando ao(a) usuário(a) que digite a frase
frase = str(input('Digite uma frase: ')).upper().strip()

# Quantas vezes aparece a letra a minúscula
print('A letra A maiúscula aparece {} vezes na frase: {}.'.format(frase.count('A'), frase))

# Em que posição a letra a aparece pela primeira vez
print('A letra A maiúscula aparece a primeira vez no índice {} na frase: {}.'.format(frase.find('A'), (frase)))

# Em que posição ela aparecer pela última vez
print('A letra A maiúscula aparece a última vez no índice {} na frase: {}.'.format(frase.rfind('A'), (frase)))
