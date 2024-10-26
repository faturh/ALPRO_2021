import pygame

pygame.init()

windows = pygame.display.set_mode(500,500)

while True :
          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                              print("anda keluar")
                              break
