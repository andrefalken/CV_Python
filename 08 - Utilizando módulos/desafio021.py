# Desafio 021
# Faça um programa em Python que abra e reproduza o áudio de um arquivo .MP3

# Importando toda a biblioteca do Pygame
import pygame

# Declarando as variáveis que receberão os nomes dos alunos
pygame.init()
pygame.mixer.music.load('Storm.mp3')
pygame.music.play()
pygame.event.wait()
