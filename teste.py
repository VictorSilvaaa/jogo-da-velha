import pygame, sys 
from scripts.button import Button
from scripts.game import *
pygame.init()

#variaveis da janela
screenSize = screenWidth, screenHeight = 720, 480
screen = pygame.display.set_mode(screenSize)
time = pygame.time.Clock()

mode1_img = pygame.image.load('img/2jogadores.png')
mode1_button = Button(236, 120, mode1_img,1)
mode2_img = pygame.image.load('img/1jogador.png')
mode2_button = Button(236, 227, mode2_img,1)

#loop variaveis
flag = True

status = 'run'
while flag:
  if status == 'run':
    #jogo roda, tem que colocar algum botão que quando clica
    #muda o valor de status para paus
  else:
    #desenha tela de pausa
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
      pygame.quit()
    
    
    
  

  
  
    
  
  pygame.display.update()
    



  