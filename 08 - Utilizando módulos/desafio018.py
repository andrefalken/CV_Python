# Desafio 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo 

# Importando toda a biblioteca de matemática
import math

# Declarando a variável para receber um ângulo qualquer 
angulo = float(input('Digite um Ângulo: '))

# Calculando e imprimindo o valor do seno, cosseno e tangente desse ângulo 
print(f'O Seno do Ângulo {angulo} é igual a {math.sin(math.radians(angulo)):.2f}.')
print(f'O Cosseno do Ângulo {angulo} é igual a {math.cos(math.radians(angulo)):.2f}.')
print(f'A Tangente do Ângulo {angulo} é igual a {math.tan(math.radians(angulo)):.2f}.')
