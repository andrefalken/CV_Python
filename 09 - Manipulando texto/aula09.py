# Imprimindo a frase 'Curso em Vídeo Python' na tela
frase = 'Curso em Vídeo Python'
print(frase)

# Imprimindo a 4ª letra da frase 'Curso em Vídeo Python' na tela
frase = 'Curso em Vídeo Python'
print(frase[3])

# Imprimindo da 4ª letra até a 12ª letra da frase 'Curso em Vídeo Python' na tela
frase = 'Curso em Vídeo Python'
print(frase[3:13])

# Imprimindo do início até a 12ª letra da frase 'Curso em Vídeo Python' na tela
frase = 'Curso em Vídeo Python'
print(frase[:13])

# Imprimindo da 12ª letra até o final da frase 'Curso em Vídeo Python' na tela
frase = 'Curso em Vídeo Python'
print(frase[13:])

# Imprimindo da 1ª letra até a 14ª letra da frase 'Curso em Vídeo Python' na tela
frase = 'Curso em Vídeo Python'
print(frase[1:15])

# Imprimindo da 1ª letra até a 14ª letra da frase pulando de dois em dois índices (letras) 'Curso em Vídeo Python' na tela
frase = 'Curso em Vídeo Python'
print(frase[1:15:2])

# Imprimindo do início até o final da frase pulando de dois em dois índices (letras) 'Curso em Vídeo Python' na tela
frase = 'Curso em Vídeo Python'
print(frase[::2])

# Imprimindo um texto longo (fica mais fácil para criar menus interativos)
print("""Wecome! Are you completely new to programmimg?
Because we're about to find why and how to get started with Python.
Fortunately, an experienced programmer in any programmimg language
(whatever it may be) can pick up Python very quickly.
It's also easy for beginners to use and learn, so jump in!""")

# Imprimindo na tela quantas vezes se repete a letra 'o' na frase 'Curso em Vídeo Python'
# Observação: são diferenciadas maiúsculas de minúsculas
frase = 'Curso em Vídeo Python'
print(frase.count('o'))

# Transformando a frase toda em maiúscula
# Imprimindo na tela quantas vezes se repete a letra 'O' na frase 'Curso em Vídeo Python'
# Observação: são diferenciadas maiúsculas de minúsculas
frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))

# Imprimindo na tela o tamanho da frase 'Curso em Vídeo Python'
frase = 'Curso em Vídeo Python'
print(len(frase))

# Imprimindo na tela o tamanho da frase 'Curso em Vídeo Python' com todos os espaços do início e fim da frase removidos
frase = '     Curso em Vídeo Python     '
print(len(frase.strip()))

# Imprimindo uma substituição de trecho da String com o comando replace
frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase)

# Verificando se a palavra 'Curso' está dentro da string 'Curso em Vídeo Python'
frase = 'Curso em Vídeo Python'
print('Curso' in frase)

# Verificando se a palavra 'Curso' está dentro da string 'Curso em Vídeo Python' mas agora mostrando que a palavra 'Curso' começa no índice 0
frase = 'Curso em Vídeo Python'
print(frase.find('Curso'))

# Verificando se a palavra 'vídeo' está dentro da string 'Curso em Vídeo Python' mas agora mostrando que a palavra 'vídeo' em minúsculo não existe
# por isso é retornado o valor -1
frase = 'Curso em Vídeo Python'
print(frase.find('vídeo'))

# Verificando se a palavra 'vídeo' está dentro da string 'Curso em Vídeo Python'
# Antes disso transformo toda a frase 'curso em vídeo' em minúsulo com a função lower, logo, encontrando o início da palavra 'vídeo' no índice 9
frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo'))

# Fatiamento e impressão em lista da string 'Curso em Vídeo Python'
frase = 'Curso em Vídeo Python'
print(frase.split())

# Fatiamento e impressão em lista do item 0 'Curso', da string 'Curso em Vídeo Python' alocado em uma variável 
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])

# Fatiamento e impressão em lista do item 2 'Vídeo', exibendo a letra 'e' (subitem 3), da string 'Curso em Vídeo Python' alocado em uma variável 
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])