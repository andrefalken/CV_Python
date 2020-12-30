# Importando apenas a função sqrt e a função floor da biblioteca de matemática
from math import sqrt, floor

# Declarando a variável para receber um número inteiro
numero = int(input('Digite um número inteiro: '))

# Declarando a variável para receber a raiz quadrada da biblioteca math neste caso, como importamos somente 2 funções, 
# você não deve digitar math.sqrt(), devendo digitar sqrt diretamente
raiz_quadrada = sqrt(numero)

# Imprimindo a raiz quadrada da variável numero: sqrt(numero) aliada a função floor (arredondamento para baixo)
print(f'A raiz quadrada de {numero} é igual a {floor(raiz_quadrada)}.')
