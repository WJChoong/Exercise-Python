import random
# user go first
# text based game

board = [' ' for x in range(10)]
# have 1 leading space so the input will correspond to the space

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print("")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("")

# bo for board, le for letter
# check each position
# check for winner
def isWinner(bo, le):
    return (
            (bo[7] == le and bo[8] == le and bo[9] == le) or 
            (bo[4] == le and bo[5] == le and bo[6] == le) or 
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or 
            (bo[2] == le and bo[5] == le and bo[8] == le) or 
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or 
            (bo[3] == le and bo[5] == le and bo[7] == le) 
            )

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        # to make sure the input is a number
        try:
            move = int (move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, this space is occupied")
            else:
                print("Please type a number within the range")
        except:
            print("Please typea number")

def compMove():
    # make a list of possible moves
    possiblesMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] # getting all the possible moves from the board
    move = 0 # initial value
    
    # run all move to see the possibility
    for let in ['O', 'X']:
        for i in possiblesMoves:
            boardCopy = board[:] # create a copy of original board
            boardCopy[i] = let # move in the position
            if isWinner(boardCopy, let): # check whether that move will win
                move = i
                return move
    
    cornersOpen = []
    for i in possiblesMoves:
        # check is there any space at the corner
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    # make sure there is a place in the corner
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possiblesMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in possiblesMoves:
        # check is there any space at the corner
        if i in [1, 3, 7, 9]:
            edgesOpen.append(i)

    # make sure there is a place in the corner
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move # return 0 is no move is done

def selectRandom(li):
    ln =  len(li)
    r = random.randrange(0, ln) # randrange start at x, ends before y   randrange(y, x)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else: 
        return True

def main():
    print(" Welcome to Tic Tac Toe! ")
    printBoard(board)

    while not (isBoardFull(board)):
        # player move
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O\'s won this time!")
            break # stop the loop since computer had won
        
        # computer move
        if not (isWinner(board, 'O')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print("X\'s won this time!")
            break # stop the loop since computer had won

    if isBoardFull(board):
        print("Tie Game!")
main()