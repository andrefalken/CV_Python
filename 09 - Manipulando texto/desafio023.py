# Desafio 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separadamente
# Ex.: 1834. Unidade: 4; Dezena:3; Centena:8; Milhar:1;

# Pedindo ao(a) usuário(a) que insira um número inteiro entre 0 e 9999
numero = int(input('Digite um número inteiro entre 0 e 9999: '))

# Declarando as variáveis de cálculo de unidade, dezena, centena e milhar
milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10

# Imprimindo os resultados em um print para cada linha
print(f'A unidade do número {numero} é: {unidade}.')
print(f'A dezena do número {numero} é: {dezena}.')
print(f'A centena do número {numero} é: {centena}.')
print(f'A milhar do número {numero} é: {milhar}.')
