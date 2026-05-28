theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
            'low-L':' ', 'low-M':' ', 'low-R':' '}

def printBoard(board):
    print(board['top-L'], '|', board['top-M'], '|', board['top-R'])
    print(board['mid-L'], '+', board['mid-M'], '+', board['mid-R']) 
    print(board['low-L'], '|', board['low-M'], '|', board['low-R']) 

def isGameOver(board):
    stem = ('top-', 'mid-', 'low-')
    suffix = ('L', 'M', 'R')
    for x in suffix: 
        if board[stem[0]+x] == board[stem[1]+x] == board[stem[2]+x]:
            print("Congratulation !!!", board[stem[0]+x], "is winner")
            return board[stem[0]+x]
           
    for x in stem:
        if board[x+suffix[0]] == board[x+suffix[1]] == board[x+suffix[2]]:
            print("Congratulation !!!", board[x+suffix[0]], "is winner")
            return board[x+suffix[0]] 
    if board[stem[0]+suffix[0]] == board[stem[1]+suffix[1]] == board[stem[2]+suffix[2]]:
        print("Congratulation !!!", board[stem[0]+suffix[0]], "is winner")
        return board[stem[0]+suffix[0]]
    if board[stem[0]+suffix[2]] == board[stem[1]+suffix[1]] == board[stem[2]+suffix[0]]:
        print("Congratulation !!!", board[stem[0]+suffix[0]], "is winner")
        return board[stem[0]+suffix[2]]
    return ' '


printBoard(theBoard)
turn = 'X'
for x in range(9):
    printBoard(theBoard)
    print('Turn for', turn,'.', 'Move on which space')
    move = input()
    while theBoard[move] != ' ':
        print('The space is occupied, please try again')
        move = input()

    theBoard[move] = turn
    result = isGameOver(theBoard)
    if result != ' ':
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

