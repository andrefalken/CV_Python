# Desafio 021
# Faça um programa em Python que abra e reproduza o áudio de um arquivo .MP3

# Importando toda a biblioteca do Pygame
import pygame

# Declarando as variáveis que darão play e irão reproduzir o arquivo .MP3 até o término
pygame.mixer.music.load('Storm.mp3')
pygame.music.play()
pygame.event.wait()
