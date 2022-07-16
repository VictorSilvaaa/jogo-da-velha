import pygame
from scripts.utils import *
time = pygame.time.Clock()

def game(screen, gameMode):
    pygame.mouse.set_pos(150, 175)

    board, boardPositionList = createBoard()
    player = 'x'

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

                result = False  
                if pygame.mouse.get_pressed()[0]:
                    if gameMode == 1 or player == 'x':
                        pos = pygame.mouse.get_pos()
                        result, newBoard = checkInput(board, boardPositionList, pos, player)
                elif player == 'o' and gameMode == 2:
                   moviment = computerMove(board, player)
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
            print('pausado')
           
        pygame.display.update()