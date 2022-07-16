import pygame
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
  rect_img = pygame.image.load('img\Rectangle.png')
  for i in range(3):
    for j in range(3):
      x, y = pygame.mouse.get_pos()
      if board[i][j] == '*':
        if positions[i][j].collidepoint((x,y)):
            if player == 'x':
              screen.blit(rect_img_x, positions[i][j])
            elif player == 'o' and gameMode == 1:
              screen.blit(rect_img_o, positions[i][j])
            else:
              screen.blit(rect_img, positions[i][j])
        else:
          screen.blit(rect_img, positions[i][j])
      elif board[i][j] == 'x':
        screen.blit(rect_img_x, positions[i][j])
      else:
        screen.blit(rect_img_o, positions[i][j])

def checkInput(board, positions, pos, player,index=0):
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
            board[i][j] = player
            flag = True
            break
      if flag == True:
        break
  return flag, board

def verifyWin(board, player):
  contRow = 0
  contColumn = 0
  contDiagonal = 0
  contDiagonalInvers = 0
  flag = False
  for i in range(3):    
    for j in range(3):
      #horizontal
      if board[i][j] == player:
        contRow += 1
        if contRow == 3:
          flag = True
          break
      #vertical
      if board[j][i] == player:
        contColumn +=1
        if contColumn == 3:
          flag = True
          break

    #diagonal
    if board[i][i] == player:
      contDiagonal+=1
      if contDiagonal == 3:
        flag = True
        break
    if board[i][-i-1] == player:
      contDiagonalInvers+=1
      if contDiagonalInvers == 3:
        flag = True
        break
    
    contColumn = 0
    contRow = 0
  return flag
    

  

      

  return board
    
def computerMove(board, player):
    # MiniMax algorithm to find the best move
    bestValue = float('inf')
    bestMove = [0,0]
    for i in range(3):
      for j in range(3):
          if board[i][j] == '*':
              board[i][j] = 'o'
              value = minimax(board, 'x')
              board[i][j] = '*'
              if value < bestValue:
                  bestValue = value
                  bestMove = [i,j]
    return bestMove

def minimax(board, cur_player):
    # Calculate the board score
    if verifyWin(board,'x'):
        return 1
    elif verifyWin(board,'o'):
        return -1
    elif isFullBoard(board):
        return 0
    # Verify if it is the maximizing or minimizing player
    if cur_player == 'x':
        bestValue = float('-inf')
        nextPlayer = 'o'
        minORmax = max
    else:
        bestValue = float('inf')
        nextPlayer = 'x'
        minORmax = min
    for i in range(3):
        for j in range(3):
            if board[i][j] == '*':
                board[i][j] = cur_player
                value = minimax(board, nextPlayer)
                board[i][j] = '*'
                bestValue = minORmax(value, bestValue)
            # In case the 'AI' finds the best possible score
            if bestValue == 1 and cur_player =='x':
                return bestValue
            if bestValue == -1 and cur_player =='o':
                return bestValue
    return bestValue


  


     
