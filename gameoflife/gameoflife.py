from time import sleep

dead = '.'
alive = 'o'
new_board = [['']*20 for i in range(10)]

def nextStage(rows, cols, board):
    for i in range(rows):
        for j in range(cols):
            if i!= 0 and j != 0 and i != rows-1 and j != cols-1:
                live_cells = 0
                if board[i - 1][j] == alive:
                    live_cells += 1
                if board[i + 1][j] == alive:
                   live_cells += 1
                if board[i][j - 1] == alive:
                    live_cells += 1
                if board[i][j + 1] == alive:
                    live_cells += 1
                if board[i - 1][j - 1] == alive:
                    live_cells += 1
                if board[i + 1][j + 1] == alive:
                    live_cells += 1
                if board[i + 1][j - 1] == alive:
                    live_cells += 1
                if board[i - 1][j + 1] == alive:
                    live_cells += 1
                
                new_board[i][j] = dead
                if board[i][j] == alive and live_cells <2:
                    new_board[i][j] = dead
                elif board[i][j] == alive and(live_cells == 2 or live_cells == 3):
                    new_board[i][j] = alive
                elif board[i][j] == alive and live_cells >3:
                    new_board[i][j] = dead
                if board[i][j]== dead and live_cells == 3:
                    new_board[i][j] = alive
            else:
                new_board[i][j] = '.'
    board = new_board[:][:]
    drawBoard(rows,cols,board)


def drawBoard(rows, cols, board):
    for i in range(rows):
        for j in range(cols):
            print(board[i][j], end='')
        print('\n')
    print('*' * 20)


def setup():
    i = 0
    board = [[0] * 20 for i in range(10)]
    with open("pattern.txt", 'r+') as f:
        for line in f:
            col = line.split()
            for j in range(len(col)):
                board[i][j] = col[j]
            i += 1
    for i in range(len(board)):
        for j in range(len(col)):
            print(board[i][j], end='')
        print('\n')
    sleep(0.5)
    print('*' * 20, flush=True)
    sleep(0.5)

    nextStage(len(board), len(col), board)
    nextStage(len(board), len(col), board)
    nextStage(len(board), len(col), board)


setup()
