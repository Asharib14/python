import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invader")
background = pygame.image.load("background.png")
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)
running = True
while running:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
         running = False
    pygame.display.update()
pygame.quit()
sys.exit()