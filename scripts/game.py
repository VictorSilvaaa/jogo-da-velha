import pygame
from scripts.utils import *
time = pygame.time.Clock()
from scripts.button import Button

def game(screen, gameMode, level):
    pygame.mouse.set_pos(150, 175)

    board, boardPositionList = createBoard()
    player = 'x'

    pause_img = pygame.image.load('img\pause.png')
    continue_img = pygame.image.load('img\play.png')
    pause_button = Button(620, 20, pause_img,1)
    continue_button = Button(650, 20, continue_img,1)

    # Game loop
    state = 'run'
    running = True
    while running:
        time.tick(30)
        screen.fill((0,0,0))
        if state == 'run':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if pause_button.clicked():
                    state = 'pause'

                result = False  
                if pygame.mouse.get_pressed()[0]:
                    if gameMode == 1 or player == 'x':
                        pos = pygame.mouse.get_pos()
                        result, newBoard = checkInput(board, boardPositionList, pos, player)
                elif player == 'o' and gameMode == 2:
                    if level == 'easy':
                        moviment = computerMove2(board)
                    else:
                        moviment = computerMove(board, player)
                    print(board)
                    result, newBoard = checkInput(board, boardPositionList, pos, player, moviment)
                
                if result:
                    board = newBoard
                    if verifyWin(board, player):
                        print(f'{player} venceu')
                        board, boardPositionList = createBoard()
                    player = 'o' if player == 'x' else 'x' 
                if isFullBoard(board):
                    board, boardPositionList = createBoard()
            drawBoard(screen, board, boardPositionList, player, gameMode)
        if state =='pause':
            continue_button.draw(screen)
            pause_button.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if continue_button.clicked():
                    state = 'run'
           
        pygame.display.update()