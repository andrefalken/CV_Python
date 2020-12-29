# Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar 
# Considere: US$1.00 = R$3.27 (Em 03/07/2017)
# Extra: Faça a conversão para US$ e para € hoje 28/12/2020  em que US$1.00 = R$5.26 e 1€ = R$6.44

# Declaração da variável que receberá a quantia que o usuário possui em reais
reais = float(input('Digite o valor que você possui em R$: '))

# Declaração da variável de conversão entre R$ e US$
dolares = reais / 3.27
dolarhoje = reais / 5.26
eurohoje = reais / 6.44

# Resultado utilizando um print para cada operação aritmética
print(f'Com o valor de R$ {reais:.2f}, você poderia comprar em 03/07/2017 o equivalente a US$ {dolares:.2f}.')
print(f'Com o valor de R$ {reais:.2f}, você poderá comprar hoje o equivalente a US$ {dolarhoje:.2f}.')
print(f'Com o valor de R$ {reais:.2f}, você poderá comprar hoje o equivalente a {eurohoje:.2f} €.')
