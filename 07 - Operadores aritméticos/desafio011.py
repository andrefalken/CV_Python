# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área equivalente a 2m²

# Declaração das variáveis que receberão a altura e a largura da parede
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

# Declaração da variável de cálculo da área e da quantidade de tinta a ser utilizada
area = altura * largura
tinta_utilizada = area / 2

# Resultado utilizando um print para a área calculada e a tinta a ser utilizada
print(f'A area entre {altura} x {largura} = {area} m², portanto, você deverá comprar {tinta_utilizada} litros de tinta.')
