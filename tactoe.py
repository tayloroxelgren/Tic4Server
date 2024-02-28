tactoeboard=[0]*9

def boardVisual(board):
    print(board[:3])
    print(board[3:6])
    print(board[6:])

def hasWinner(board):
    if all(element == 1 for element in board[:3]) \
    or all(element == 1 for element in board[3:6])\
    or all(element == 1 for element in board[6:])\
    or all(element == 1 for element in [board[0],board[4],board[8]])\
    or all(element == 1 for element in [board[8],board[4],board[0]])\
    or all(element == 1 for element in [board[0],board[3],board[6]])\
    or all(element == 1 for element in [board[2],board[5],board[8]]):
        return True, 1

    if all(element == 2 for element in board[:3]) \
    or all(element == 2 for element in board[3:6])\
    or all(element == 2 for element in board[6:])\
    or all(element == 2 for element in [board[0],board[4],board[8]])\
    or all(element == 2 for element in [board[8],board[4],board[0]])\
    or all(element == 2 for element in [board[0],board[3],board[6]])\
    or all(element == 2 for element in [board[2],board[5],board[8]]):
        return True, 2

    return False,None

# Temporary function that for now accepts input over command line but will have different functionality later
def gatherMove():
    return int(input())

# Player 1 will always go first
def playGame(board):
    turn=0
    while(hasWinner(tactoeboard)[0]==False and turn<9):
        isEven=turn%2
        moveCmd=gatherMove()
        print(board[moveCmd])
        if board[moveCmd]==0:
            if(isEven):
                board[moveCmd]=2
            else:
                board[moveCmd]=1

            boardVisual(tactoeboard)
            turn+=1
        else:
            print("Move not allowed")
        
    


boardVisual(tactoeboard)
playGame(tactoeboard)

