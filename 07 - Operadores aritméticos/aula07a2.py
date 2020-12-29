# Declaração das variáveis que pedem o número a ser digitado pelo usuário
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

# Declaração das variáveis que recebem as operações aritméticas
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 /  n2
divisaointeira = n1 // n2
potenciacao = n1 ** n2

# Resultando usando a \n (quebra de linha) no lugar de vários prints
print(f'A soma entre {n1} e {n2} é igual a {soma}. \nO produto entre {n1} e {n2} é igual a {multiplicacao}. \nA divisão entre {n1} e {n2} é igual a {divisao}. \nA divisão inteira entra {n1} e {n2} é igual a {divisaointeira}. \nA potência entre {n1} e {n2} é igual a {potenciacao}')
