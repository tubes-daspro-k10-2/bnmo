from typing import final


def tictactoe():
    gameEnd = False
    playerXTurn = True # X then O in that order

    gameTable = [['#' for i in range(3)] for j in range(3)]

    while not gameEnd:
        printTable(gameTable)
        print()
        if playerXTurn:
            gameTable = fillTable('X', gameTable)
        else:
            gameTable = fillTable('O', gameTable)

        if checkWinner(gameTable) != '#':
            print(checkWinner(gameTable), 'won!')
            gameEnd = True

        elif isGameTableFull(gameTable):
            gameEnd = True
            print('Permainan selesai, Hasil Draw!')

        else :
            playerXTurn = not playerXTurn
        print()
    
    printTable(gameTable)

def isGameTableFull(gameTableToCheck : list[list[int]]) -> bool:
    for i in range(3):
        for j in range(3):
            if gameTableToCheck[i][j] == '#':
                return False
    return True

def printTable(gameTableToPrint):
    print('  123 X')
    for i in range(3):
        print(i+1, end=' ')
        for j in range(3):
            print(gameTableToPrint[j][i], end='')
        print()
    print('Y')

def checkWinner(gameTableToCheck):
    #horizontal/vertical win
    for i in range(3):
        if gameTableToCheck[i][0] == gameTableToCheck[i][1] == gameTableToCheck[i][2] != '#':
            return gameTableToCheck[i][0]
        elif gameTableToCheck[0][i] == gameTableToCheck[1][i] == gameTableToCheck[2][i] != '#':
            return gameTableToCheck[0][i]
    
    # diagonal win
    if gameTableToCheck[0][0] == gameTableToCheck[1][1] == gameTableToCheck[2][2] != '#':
        return gameTableToCheck[0][0]
    elif gameTableToCheck[2][0] == gameTableToCheck[1][1] == gameTableToCheck[0][2] != '#':
        return gameTableToCheck[2][0]

    return '#' # no one won

def fillTable(player = 'default', newGameTable = [['a' for i in range(3)] for j in range(3)]) -> int:
    inputValid = False

    while not inputValid:
        print('giliran pemain', player)
        try:
            x = int(input('X : ')) - 1
            y = int(input('Y : ')) - 1
        except:
#            print('input tidak valid')1
            print()
            pass
        else:
            if 0 <= x <= 2 and 0 <= y <= 2:
                if newGameTable[x][y] == '#':
                    inputValid = True
                else:
                    print(' sudah terisi cobalagi'); 
                    print()
            else:
                print('print tidak valid cobalagi')
                print()

    newGameTable[x][y] = player
    return newGameTable

tictactoe()
#print(updateTable())
#print(True == False == False)