# Declaração das variáveis que pedem o número a ser digitado pelo usuário
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

# Declaração das variáveis que recebem as operações aritméticas
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 /  n2
divisaointeira = n1 // n2
potenciacao = n1 ** n2

# Resultado utilizando um print para cada operação aritmética
print(f'A soma entre {n1} e {n2} é igual a {soma}.')
print(f'O produto entre {n1} e {n2} é igual a {multiplicacao}.')
print(f'A divisão entre {n1} e {n2} é igual a {divisao}.')
print(f'A divisão inteira entra {n1} e {n2} é igual a {divisaointeira}.')
print(f'A potência entre {n1} e {n2} é igual a {potenciacao}')
