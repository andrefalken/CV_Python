# Desafio 008
# Escreva um programa que leia um valor em metros e exiba a conversão em centímetros e milímetros
# Extra: converta também em quilômetros, hectômetros, decâmetros e decímetros

# Declaração da variável que receberá o valor em metros
metros = float(input('Digite o valor em metros: '))

# Declaração das variáveis que farão as conversões em centímetros e milímetros
quilometros = metros / 1000
hectometros = metros / 100
decametros = metros / 10
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000

# Resultado utilizando um print para cada conversão
print(f'A conversão de {metros} metros em quilômetros é igual a {quilometros} quilômetros.')
print(f'A conversão de {metros} metros em hectômetros é igual a {hectometros} hectômetros.')
print(f'A conversão de {metros} metros em decâmetros é igual a {decametros} decâmetros.')
print(f'A conversão de {metros} metros em decímetros é igual a {decimetros} decímetros.')
print(f'A conversão de {metros} metros em centímetros é igual a {centimetros} centímetros.')
print(f'A conversão de {metros} metros em milímetros é igual a {milimetros} milímetros.')
