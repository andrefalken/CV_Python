# Desafio 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e 
# calcule e mostre o comprimento da hipotenusa

# Importando toda a biblioteca de matemática
import math

# Declarando a variável para receber o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('Digite o comprimento do cateto adjacente: '))

# Calculando e imprimindo o comprimento da hipotenusa
print(f'O comprimento da hipotenusa é igual a {math.hypot(a, b):.2f}.')
