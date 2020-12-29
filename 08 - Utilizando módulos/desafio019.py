# Desafio 019
# Um professor que sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que o ajude lendo o nome dos alunos e escrevendo o nome do escolhido

# Importando toda a biblioteca aleatória (random)
import random

# Declarando as variáveis que receberão os nomes dos alunos
aluno1 = input('Digite o nome do(a) aluno(a) 1: ')
aluno2 = input('Digite o nome do(a) aluno(a) 2: ')
aluno3 = input('Digite o nome do(a) aluno(a) 3: ')
aluno4 = input('Digite o nome do(a) aluno(a) 4: ')

# Declarando a variável e a função random que irá sortear o aluno
escolhido = random.choice([aluno1, aluno2, aluno3, aluno4])

# Imprimindo o aluno que irá apagar o quadro
print(f'O(A) aluno(a) que irá apagar o quadro é o(a) {escolhido}. Parabéns {escolhido}!')
