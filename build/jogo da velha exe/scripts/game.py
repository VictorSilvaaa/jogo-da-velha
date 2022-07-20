import pygame
from scripts.utils import *
from scripts.button import Button

time = pygame.time.Clock()
music_background = pygame.mixer.Sound('sounds\\fundo.wav')
music_channel= pygame.mixer.Channel(0)

#variables button/img
pause_img = pygame.image.load('img\pause.png')
continue_img = pygame.image.load('img\play.png')
pause_button = Button(620, 20, pause_img,1)
continue_button = Button(650, 20, continue_img,1)

def game(screen, gameMode, level):
    
    fonte = pygame.font.SysFont('arial',25, True,True)
    music_channel.play(music_background,-1)
    pygame.mouse.set_pos(0, 0)

    #init board game
    board, boardPositionList = createBoard()
    player = 'x'
    scoreX = 0
    scoreO = 0

    # Game loop
    state = 'run'
    running = True
    while running:
        time.tick(30)
        screen.fill((0,0,0))
        if state == 'run':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    music_channel.stop()
                    running = False
                if pause_button.clicked():
                    state = 'pause'

                result = False  
                if gameMode == 1 or player == 'x':
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        result, newBoard = checkInput(board, boardPositionList, pos, player)
                else:
                    if level == 'easy':
                        moviment = computerMoveEasy(board)
                    else:
                        moviment = computerMove(board, player)
                    result, newBoard = checkInput(board, boardPositionList, pos, player, moviment)
                
                if result:
                    board = newBoard
                    if verifyWin(board, player):
                        if player == 'x':
                            scoreX += 1
                        else:
                            scoreO += 1
                        board, boardPositionList = createBoard()
                    player = 'o' if player == 'x' else 'x' 
                    if isFullBoard(board):
                        board, boardPositionList = createBoard()

            drawBoard(screen, board, boardPositionList, player, gameMode)
            pause_button.draw(screen)
            text_formated = fonte.render(f'X= {scoreX} | O= {scoreO}',True,(255,255,255))
            screen.blit(text_formated,(0,0))
        if state =='pause':
            screen.fill((0,0,0))
            continue_button.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    music_channel.stop()
                    running = False
                if continue_button.clicked():
                    state = 'run'
           
        pygame.display.update()