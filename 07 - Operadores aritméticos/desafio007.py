# Desafio 007
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

# Declaração da variável que receberá o as notas digitadas pelo usuário
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Declaração da variável que receberá a média
media = (n1 + n2) / 2 

# Resultado utilizando um print para cada operação aritmética
print(f'A média entre {n1} e {n2} é igual a {media:.1f}.')
