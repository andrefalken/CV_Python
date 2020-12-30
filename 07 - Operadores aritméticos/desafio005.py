# Desafio 005
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

# Declaração da variável que receberá o número inteiro digitado pelo usuário
n = int(input('Digite um número inteiro: '))

# Declaração das variáveis que recebem as operações aritméticas
antecessor = n - 1
sucessor = n + 1

# Resultado utilizando um print para cada operação aritmética
print(f'O antecessor de {n} é igual a {antecessor}.')
print(f'O sucessor de {n} é igual a {sucessor}.')
