# Desafio 015
# Escreva um programa que pergunte a quantidade de km percorridos por um caro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço à pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado

# Declaração das variáveis que pedem o número de diárias contratadas e a km percorrida
diarias = int(input('Digite o número de diárias contratadas: '))
km = float(input('Digite a km percorrida: '))

# Declaração da variável que calcula o preço a pagar
total_diarias = diarias * 60
total_km = km * 0.15
total_pagar = total_diarias + total_km

# Resultado utilizando um print para a temperatura em ºF
print(f'Você contratou {diarias} diárias e percorreu {km:.1f}km totalizando um valor à pagar no total de R${total_pagar:.2f}.')
