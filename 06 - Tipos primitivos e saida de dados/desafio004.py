# Desafio 004
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele 
n = input('Digite algo: ')
print(f'O tipo primitivo de N é {type(n)}.')
print(f'É uma caractere do alfabeto? {n.isalpha()}.')
print(f'É um caractere do formato ASCI? {n.isascii()}.')
print(f'É um caractere do tipo decimal? {n.isdecimal()}.')
print(f'É um caractere do tipo dígito? {n.isdigit()}.')
print(f'É um caractere do tipo identificador? {n.isidentifier()}.')
print(f'É um caractere do tipo minúsculo? {n.islower()}.')
print(f'É um caractere numérico? {n.isnumeric()}.')
print(f'É um caractere possível de imprimir? {n.isprintable()}.')
print(f'É um caractere do tipo espaço? {n.isspace()}.')
print(f'É um caractere do tipo título? {n.istitle()}.')
print(f'É um caractere do tipo maiúsculo? {n.isupper()}.')