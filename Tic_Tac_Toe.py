# tic tac toe

import random

positions = []
gameBox = []
user = ""
system = ""
user1 = "X"
user2 = "O"


# start
def initializeGame(gameSelect):
    if gameSelect == 1:
        for i in range(0, 9):
            positions.append(i)
            gameBox.append(" ")
    else:
        for i in range(0, 16):
            positions.append(i)
            gameBox.append(" ")


def printGameBox(gameSelect):
    # print(gameBox)
    if gameSelect == 1:
        print('   |   |')
        print(' ' + gameBox[0] + ' | ' + gameBox[1] + ' | ' + gameBox[2])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + gameBox[3] + ' | ' + gameBox[4] + ' | ' + gameBox[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + gameBox[6] + ' | ' + gameBox[7] + ' | ' + gameBox[8])
        print('   |   |')
    else:
        # print(gameBox)
        print('   |   |   |')
        print(' ' + gameBox[0] + ' | ' + gameBox[1] + ' | ' + gameBox[2] + ' | ' + gameBox[3])
        print('   |   |   |')
        print('---------------')
        print('   |   |   |')
        print(' ' + gameBox[4] + ' | ' + gameBox[5] + ' | ' + gameBox[6] + ' | ' + gameBox[7])
        print('   |   |   |')
        print('---------------')
        print('   |   |   |')
        print(' ' + gameBox[8] + ' | ' + gameBox[9] + ' | ' + gameBox[10] + ' | ' + gameBox[11])
        print('   |   |   |')
        print('---------------')
        print('   |   |   |')
        print(' ' + gameBox[12] + ' | ' + gameBox[13] + ' | ' + gameBox[14] + ' | ' + gameBox[15])
        print('   |   |   |')


def userMove(user):
    while True:
        try:
            move = int(raw_input("Select a move among " + str(positions) + " : "))
        except ValueError:
            print("Invalid Move")
            continue
        if move in positions:
            gameBox[move] = user
            positions.remove(move)
            break
        else:
            print("Invalid Move")
            continue


def checkWinCondition(gameSelect, msg, user):
    if gameSelect == 1:
        if (gameBox[0] == gameBox[1] == gameBox[2] == user
                or gameBox[2] == gameBox[5] == gameBox[8] == user
                or gameBox[3] == gameBox[4] == gameBox[5] == user
                or gameBox[6] == gameBox[7] == gameBox[8] == user
                or gameBox[0] == gameBox[3] == gameBox[6] == user
                or gameBox[1] == gameBox[4] == gameBox[7] == user
                or gameBox[0] == gameBox[4] == gameBox[8] == user
                or gameBox[2] == gameBox[4] == gameBox[6] == user):
            print(msg + "Wins!!!")
            return True
        else:
            if positions == []:
                print ("It's a Tie")
                return True
            else:
                return False

    else:
        if (gameBox[0] == gameBox[1] == gameBox[2] == gameBox[3] == user
                or gameBox[4] == gameBox[5] == gameBox[6] == gameBox[7] == user
                or gameBox[8] == gameBox[9] == gameBox[10] == gameBox[11] == user
                or gameBox[12] == gameBox[13] == gameBox[14] == gameBox[15] == user
                or gameBox[0] == gameBox[4] == gameBox[8] == gameBox[12] == user
                or gameBox[1] == gameBox[5] == gameBox[9] == gameBox[13] == user
                or gameBox[2] == gameBox[6] == gameBox[10] == gameBox[14] == user
                or gameBox[3] == gameBox[7] == gameBox[11] == gameBox[15] == user
                or gameBox[0] == gameBox[5] == gameBox[10] == gameBox[15] == user
                or gameBox[3] == gameBox[6] == gameBox[9] == gameBox[12] == user):
            print(msg + "Wins!!!")
            return True
        else:
            if positions == []:
                print ("It's a Tie")
                return True
            else:
                return False


def checkWin(gameSelect, user):
    if gameSelect == 1:
        if (gameBox[0] == gameBox[1] == gameBox[2] == user
                or gameBox[2] == gameBox[5] == gameBox[8] == user
                or gameBox[3] == gameBox[4] == gameBox[5] == user
                or gameBox[6] == gameBox[7] == gameBox[8] == user
                or gameBox[0] == gameBox[3] == gameBox[6] == user
                or gameBox[1] == gameBox[4] == gameBox[7] == user
                or gameBox[0] == gameBox[4] == gameBox[8] == user
                or gameBox[2] == gameBox[4] == gameBox[6] == user):
            return True
        else:
            return False

    else:
        if (gameBox[0] == gameBox[1] == gameBox[2] == gameBox[3] == user
                or gameBox[4] == gameBox[5] == gameBox[6] == gameBox[7] == user
                or gameBox[8] == gameBox[9] == gameBox[10] == gameBox[11] == user
                or gameBox[12] == gameBox[13] == gameBox[14] == gameBox[15] == user
                or gameBox[0] == gameBox[4] == gameBox[8] == gameBox[12] == user
                or gameBox[1] == gameBox[5] == gameBox[9] == gameBox[13] == user
                or gameBox[2] == gameBox[6] == gameBox[10] == gameBox[14] == user
                or gameBox[3] == gameBox[7] == gameBox[11] == gameBox[15] == user
                or gameBox[0] == gameBox[5] == gameBox[10] == gameBox[15] == user
                or gameBox[3] == gameBox[6] == gameBox[9] == gameBox[12] == user):

            return True
        else:
            return False


def expertMove(user, gameSelect):
    if gameSelect == 1:
        size = 3
    else:
        size = 4

    for i in positions:
        gameBox[i] = user
        if checkWin(gameSelect, user):
            gameBox[i] = " "
            return i
        gameBox[i] = " "
    return random.choice(positions)


def playWithComputer(gameSelect, difSelect):
    turn = raw_input("Enter \"Y\" to go first\n")

    while True:
        if turn.lower() == 'y':
            while True:
                user = "X"
                system = "O"
                printGameBox(gameSelect)
                userMove(user)
                if checkWinCondition(gameSelect, "Player ", user):
                    printGameBox(gameSelect)
                    return
                printGameBox(gameSelect)
                if difSelect == 1:
                    move = random.choice(positions)

                else:
                    move = expertMove(user, gameSelect)

                gameBox[move] = system
                positions.remove(move)
                print("System's Move : ")

                if checkWinCondition(gameSelect, "System ", system):
                    printGameBox(gameSelect)
                    return

        else:
            while True:
                system = "X"
                user = "O"
                printGameBox(gameSelect)
                if difSelect == 1:
                    move = random.choice(positions)
                else:
                    move = expertMove(user, gameSelect)

                gameBox[move] = system
                positions.remove(move)
                print("System's Move : ")

                if checkWinCondition(gameSelect, "System ", system):
                    printGameBox(gameSelect)
                    return
                printGameBox(gameSelect)
                userMove(user)
                if checkWinCondition(gameSelect, "Player ", user):
                    printGameBox(gameSelect)
                    return


def playAmongUsers(gameSelect):
    while True:
        printGameBox(gameSelect)
        userMove(user1)
        if checkWinCondition(gameSelect, "Player1 ", user1):
            printGameBox(gameSelect)
            return
        printGameBox(gameSelect)
        userMove(user2)
        if checkWinCondition(gameSelect, "Player2 ", user2):
            printGameBox(gameSelect)
            return


while True:
    # game selection
    positions = []
    gameBox = []
    try:
        gameSelect = int(raw_input("Select the game\n 1. 3 X 3 \n 2. 4 X 4 \n 3. Quit\n"))
    except ValueError:
        print("Invalid Selection")
        continue
    if gameSelect not in (1, 2, 3):
        print("Invalid input")
        continue
    else:
        if gameSelect == 3:
            break
        try:
            modeSelect = int(raw_input("Select the mode of play:\n 1. Single Player \n 2. Two Player\n"))
        except ValueError:
            print("Invalid Mode")
            continue
        if modeSelect not in (1, 2):
            print("Invalid input")
            continue
        else:
            if modeSelect == 1:
                try:
                    difSelect = int(raw_input("Select the difficulty:\n 1. Beginner \n 2. Expert\n"))
                except ValueError:
                    print("Invalid Selection")
                    continue
                if difSelect not in (1, 2):
                    print("Invalid input")
                    continue
                else:
                    initializeGame(gameSelect)
                    playWithComputer(gameSelect, difSelect)
            else:
                initializeGame(gameSelect)
                playAmongUsers(gameSelect)

    if raw_input("Play Again? Y/N ").lower() != "y":
        break
