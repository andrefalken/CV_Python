# Desafio 016
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira

# Importando toda a biblioteca de matemática
import math

# Declarando a variável para receber um número real
numero = float(input('Digite um número real: '))

# Imprimindo parte inteira do número real digitado pelo usuário
print(f'A parte inteira do número {numero} é igual a {math.floor(numero)}.')
