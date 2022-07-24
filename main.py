import pygame, sys 
from scripts.button import Button
from scripts.game import *
from time import sleep

pygame.init()
#variables window
screenSize = screenWidth, screenHeight = 720, 480
screen = pygame.display.set_mode(screenSize)
time = pygame.time.Clock()
textHome = pygame.image.load('img\\textJogodaVelha.png')

#mode 1 -> two players || mode 2 -> player vs computer
mode1_img = pygame.image.load('img/2jogadores.png')
mode1_button = Button(236, 120, mode1_img,1)
mode2_img = pygame.image.load('img/1jogador.png')
mode2_button = Button(236, 227, mode2_img,1)

#mode 2 buttons/imgs
easy_img = pygame.image.load('img\EASY.png')
back_img = pygame.image.load('img\\back.png')
easy_button = Button(235, 120, easy_img,1)
back_button = Button(235, 260, back_img,1)

pygame.mixer.init()
music = pygame.mixer.music.load('sounds/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

#loop variaveis
flag = True
state = 'home'
while flag:
  time.tick(30)
  if state == 'home':
    if not pygame.mixer.music.get_busy():
      pygame.mixer.music.play(-1)
    screen.fill((52,78,91))
    screen.blit(textHome, (266,25))
    #button options mode game
    mode1_button.draw(screen)
    mode2_button.draw(screen)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
        pygame.quit()
      if mode1_button.clicked():
        pygame.mixer.music.stop()
        game(screen, 1,None)
      if mode2_button.clicked():
        state = 'level'
        sleep(0.25)
  else:
    screen.fill((52,78,91))
    easy_button.draw(screen)
    back_button.draw(screen)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        flag = False
        sys.exit()
        pygame.quit()
      if easy_button.clicked():
        pygame.mixer.music.stop()
        game(screen, 2, 'easy')
        state ='home'       
      if back_button.clicked():
        state ='home'


  pygame.display.update()
    



  