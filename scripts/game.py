import pygame
from scripts.utils import *
from scripts.button import Button
from time import sleep
time = pygame.time.Clock()
music_background = pygame.mixer.Sound('sounds/fundo.wav')
music_channel= pygame.mixer.Channel(0)

#variables button/img
pause_img = pygame.image.load('img/pause.png')
break_img = pygame.image.load('img/break.png')
continue_img = pygame.image.load('img/play.png')
pause_button = Button(610, 20, pause_img,1)
break_button = Button(650, 20, break_img,1)
continue_button = Button(610, 20, continue_img,1)



def game(screen, gameMode, level):
    
    fonte = pygame.font.SysFont('arial',25, True,True)
    music_channel.play(music_background,-1)
    pygame.mouse.set_pos(0, 0)

    #init board game
    board, boardPositionList = createBoard()
    player = 'x'
    scoreX = 0
    scoreO = 0

    #init poderes
    powerX = 1
    powerO = 1
    powerFlagX = False 
    powerFlagO= False
    power_img = pygame.image.load('img\\2vs.png')
    power_button = Button(44,180,power_img,1)

    # Game loop
    state = 'run'
    running = True
    while running:
        time.tick(30)
        screen.fill((52,78,91))
        if state == 'run':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    music_channel.stop()
                    running = False
                if pause_button.clicked():
                    state = 'pause'
                if break_button.clicked():
                    music_channel.stop()
                    running = False
                if power_button.clicked() and player =='x' and powerX>0 and gameMode == 1:
                    powerFlagX = True
                elif power_button.clicked() and player =='o' and powerO>0 and gameMode == 1:
                    powerFlagO = True


                result = False  
                if gameMode == 1 or player == 'x':
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        result, newBoard = checkInput(board, boardPositionList, pos, player)
                else:
                    if level == 'easy':
                        moviment = computerMoveEasy(board)
                        result, newBoard = checkInput(board, boardPositionList, pos, player, moviment)                     
                if result:
                    board = newBoard
                    if verifyWin(board, player):
                        if player == 'x':
                            scoreX += 1
                            if scoreX == 3:
                                board, boardPositionList = createBoard()
                                scoreX = 0
                                scoreO = 0
                        else:
                            scoreO += 1
                            if scoreO == 3:
                                board, boardPositionList = createBoard()
                                scoreX = 0
                                scoreO = 0
                        sleep(1)
                        board, boardPositionList = createBoard()
                    if isFullBoard(board):
                        board, boardPositionList = createBoard()
                       
                    if powerFlagX:
                        powerX -=1
                        powerFlagX = False
                    elif powerFlagO:
                        powerO -=1
                        powerFlagO = False
                    else:
                        player = 'o' if player == 'x' else 'x' 
            
            drawBoard(screen, board, boardPositionList, player, gameMode)
            #draw power if player power is > 0
            if gameMode == 1:
                if player == 'x' and scoreX<scoreO and powerX>0:
                    power_button.draw(screen)
                elif player == 'o' and scoreO<scoreX and powerO>0:
                    power_button.draw(screen)
            pause_button.draw(screen)
            break_button.draw(screen)
            
            text_Score = fonte.render(f'X= {scoreX} || O= {scoreO}',True,(255,255,255))
            text_Player = fonte.render(f'É a vez de {player}',True,(255,255,255))
            screen.blit(text_Score,(10,10))
            screen.blit(text_Player,(275,400))
        
        if state =='pause':
            continue_button.draw(screen)
            break_button.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    music_channel.stop()
                    running = False
                if continue_button.clicked():
                    state = 'run'
                if break_button.clicked():
                    music_channel.stop()
                    running = False
           
        pygame.display.update()