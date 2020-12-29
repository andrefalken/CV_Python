# Desafio 006
# Crie um algoritmo que leia um número e mostre seu dobro, seu triplo e sua raiz quadrada

# Declaração da variável que receberá o número inteiro digitado pelo usuário
n = int(input('Digite um número inteiro: '))

# Declaração das variáveis que recebem as operações aritméticas
dobro = n * 2
triplo = n * 3
raizQ = n ** 0.5

# Resultado utilizando um print para cada operação aritmética
print(f'O dobro de {n} é igual a {dobro}.')
print(f'O triplo de {n} é igual a {triplo}.')
print(f'A raiz quadrada de {n} é igual a {raizQ:.2f}.')
