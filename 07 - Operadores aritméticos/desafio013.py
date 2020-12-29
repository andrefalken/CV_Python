# Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

# Listagem de salários de funcionários antes do aumento de 15%
print ('-' * 165)
print ('Salários dos funcionários antes do aumento de 15 por cento:')
print ('Funcionário 1: Programador Sênior: Salário de R$ 5000.00.')
print ('Funcionário 2: Pentester: Salário de R$ 1999.90.')
print ('Funcionário 3: Gestor de Redes: Salário de R$ 1999.90.')
print ('-' * 165)

# Declaração das variáveis do cálulo do novo salário
funcionário1 = (15 / 100) * 5000
funcionario2 = (15 / 100) * 1999.90
funcionario3 = (15 / 100) * 1999.90

# Resultado utilizando um print para cada operação aritmética
print ('-' * 165)
print ('Salários dos funcionários após o aumento de 15 por cento:')
print(f'Funcionário 1: Programador Sênior: Salário de R$ 5000.00, passa a ser de R${5000 + funcionário1:.2f}.')
print(f'Funcionário 2: Pentester: Salário de R$ 1999.90, passa a ser de R${1999.90 + funcionario2:.2f}.')
print(f'Funcionário 3: Gestor de Redes: Salário de R$ 1999.90, passa a ser de R${1999.90 + funcionario3:.2f}.')
print ('-' * 165)
