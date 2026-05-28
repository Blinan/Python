
theBoard = {
'8a':'', '8b':'', '8c':'', '8d':'', '8e':'', '8f':'', '8g':'', '8h':''
'7a':'', '7b':'', '7c':'', '7d':'', '7e':'', '7f':'', '7g':'', '7h':''
'6a':'', '6b':'', '6c':'', '6d':'', '6e':'', '6f':'', '6g':'', '6h':''
'5a':'', '5b':'', '5c':'', '5d':'', '5e':'', '5f':'', '5g':'', '5h':''
'4a':'', '4b':'', '4c':'', '4d':'', '4e':'', '4f':'', '4g':'', '4h':''
'3a':'', '3b':'', '3c':'', '3d':'', '3e':'', '3f':'', '3g':'', '3h':''
'2a':'', '2b':'', '2c':'', '2d':'', '2e':'', '2f':'', '2g':'', '2h':''
'1a':'', '1b':'', '1c':'', '1d':'', '1e':'', '1f':'', '1g':'', '1h':''
}





def isValidChessBoard(board):
    return True


def creatBoard():
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    board = []
    for i in range(8):
        x=8-i
        rank = []
        for y in letter:
            rank.append(f'\'{x}{y}\':\'\'')
        board.append(rank)

    return board

def printBoard(board):
    for rank in board:
        print(rank)


theBoard = creatBoard()
printBoard(theBoard)
