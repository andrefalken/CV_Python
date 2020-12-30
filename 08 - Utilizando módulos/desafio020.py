# Desafio 020
# Um professor que sortear a ordem de apresentação de trabalhos dos alunos
# Faça um programa que o ajude lendo o nome dos quatro alunos e mostre a ordem sorteada

# Importando toda a biblioteca aleatória (random)
import random

# Declarando as variáveis que receberão os nomes dos alunos
aluno1 = input('Digite o nome do(a) aluno(a) 1: ')
aluno2 = input('Digite o nome do(a) aluno(a) 2: ')
aluno3 = input('Digite o nome do(a) aluno(a) 3: ')
aluno4 = input('Digite o nome do(a) aluno(a) 4: ')

# Declarando a variável e a função random que irá sortear o aluno
escolhido = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(escolhido)

# Imprimindo o aluno que irá apagar o quadro
print(f'O trabalho será apresentado na seguinte ordem: {escolhido}.')
