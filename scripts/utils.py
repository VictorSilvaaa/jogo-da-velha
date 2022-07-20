import pygame
import copy
def createBoard():
    board = [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*'],
    ]

    spaceColumn = 0
    spaceRow = 0
    boardPositionList = []
    for i in range(3):
      row = []
      for j in range(3):
        rect = pygame.Rect((188+spaceColumn, 85+spaceRow), (105, 97))
        row.append(rect)
        spaceColumn+= 105 +5
      boardPositionList.append(row)
      spaceColumn = 0
      spaceRow += 97 +5
    return board, boardPositionList

def isFullBoard(board):
  flag = True
  for i in range(3):
    for j in range(3):
      if board[i][j] == '*':
        flag = False
  return flag

rect_img = pygame.image.load('img\Rectangle.png')
rect_img_x = pygame.image.load('img\Rectanglex.png')
rect_img_o = pygame.image.load('img\Rectangleo.png')
def drawBoard(screen, board, positions, player,gameMode):
  board = copy.deepcopy(board)
  positions = copy.deepcopy(positions)
  for i in range(3):
    for j in range(3):
      mouseX, mouseY= pygame.mouse.get_pos()
      if board[i][j] == '*':
        if positions[i][j].collidepoint((mouseX, mouseY)):
            if player == 'x':
              screen.blit(rect_img_x, positions[i][j])
            elif gameMode == 1:
              screen.blit(rect_img_o, positions[i][j])
            else:
              screen.blit(rect_img, positions[i][j])
        else:
          screen.blit(rect_img, positions[i][j])
      elif board[i][j] == 'x':
        screen.blit(rect_img_x, positions[i][j])
      else:
        screen.blit(rect_img_o, positions[i][j])

pygame.mixer.init()
music_false = pygame.mixer.Sound('sounds\selectedFalse.mp3')
music_true = pygame.mixer.Sound('sounds\selected.wav')
def checkInput(board, positions, pos, player,index=0):
  board = copy.deepcopy(board)
  positions = copy.deepcopy(positions)
  flag =  False
  if index != 0:
    if board[index[0]][index[1]] == '*':
      board[index[0]][index[1]] = player
      flag = True
  else:
    for i in range(3):
      for j in range(3):
        if positions[i][j].collidepoint(pos):
          if board[i][j] == '*':
            music_true.play()
            board[i][j] = player
            flag = True
            break
          else:
            music_false.play()
      if flag == True:
        break
  return flag, board

def verifyWin(board, player):
  board = copy.deepcopy(board)
  contRow = 0
  contColumn = 0
  contDiagonal = 0
  contDiagonalInvers = 0
  for i in range(3):    
    for j in range(3):
      #horizontal
      if board[i][j] == player:
        contRow += 1
        if contRow == 3:
          return True
      
      #vertical
      if board[j][i] == player:
        contColumn +=1
        if contColumn == 3:
          return True

    #diagonal
    if board[i][i] == player:
      contDiagonal+=1
      if contDiagonal == 3:
        return True
    if board[i][-i-1] == player:
      contDiagonalInvers+=1
      if contDiagonalInvers == 3:
        return True
    
    contColumn = 0
    contRow = 0
  return False

def computerMoveEasy(board):
  board = copy.deepcopy(board)
  for i in range(3):
    for j in range(3):
      if board[i][j] == '*':
        bestMove = [i,j]
        board[i][j] = 'o'
        if verifyWin(board, 'o'):
          bestMove = [i,j]
          return bestMove
        else:
          board[i][j] = 'x'
          if verifyWin(board, 'x'):
            bestMove = [i,j]
            return bestMove
  return bestMove

     
