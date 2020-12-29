# Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

# Listagem de produtos disponíveis para compra com desconto de 5%
print ('Itens com promoção de 5 por cento de desconto: \n')
print ('Item 1: Notebook Acer Nitro 5 por R$ 5000.00.')
print ('Item 2: TV JVC 40" por R$ 1399.90.')
print ('Item 3: Action Cam Go Pro Hero 4 por R$ 799.90. \n')

item = int(input('Digite o número do item ao qual você deseja comprar com 5 por cento de desconto: '))

# Declaração das variáveis do cálulo do desconto
notebook = (5 / 100) * 5000
tv = (5 / 100) * 1399.90
camera = (5 / 100) * 799.90

# Resultado utilizando um print para cada operação aritmética
if item == 1:
    print(f'\nItem 1: Notebook Acer Nitro 5 custava R$ 5000.00, com 5 por centro de desconto ele será vendido por R${5000 - notebook:.2f}.')

elif item == 2:
    print(f'\nItem 2: TV JVC 40" custava R$ 1399.90, com 5 por centro de desconto ele será vendido por R${1399.90 - tv:.2f}.')

elif item == 3:
    print(f'\nItem 3: Action Cam Go Pro Hero 4 custava R$ 799.90, com 5 por centro de desconto ele será vendido por R${799.90 - camera:.2f}.')
