import random

print("Welcome to TicTacToe")
print("--------------------")

posible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_board = [1, 2, 3], [4, 5, 6], [7, 8, 9]
rows = 3
cols = 3


def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", game_board[x][y], end=" |")
    print("\n+---+---+---+")


def modify_array(num, turn):
    num -= 1
    if num == 0:
        game_board[0][0] = turn
    elif num == 1:
        game_board[0][1] = turn
    elif num == 2:
        game_board[0][2] = turn
    elif num == 3:
        game_board[1][0] = turn
    elif num == 4:
        game_board[1][1] = turn
    elif num == 5:
        game_board[1][2] = turn
    elif num == 6:
        game_board[2][0] = turn
    elif num == 7:
        game_board[2][1] = turn
    elif num == 8:
        game_board[2][2] = turn


def checkForWinner(gameBoard):
    # X axis
    if gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X":
        print("X has won!")
        return "X"
    elif gameBoard[0][0] == "O" and gameBoard[0][1] == "O" and gameBoard[0][2] == "O":
        print("O has won!")
        return "O"
    elif gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X":
        print("X has won!")
        return "X"
    elif gameBoard[1][0] == "O" and gameBoard[1][1] == "O" and gameBoard[1][2] == "O":
        print("O has won!")
        return "O"
    elif gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X":
        print("X has won!")
        return "X"
    elif gameBoard[2][0] == "O" and gameBoard[2][1] == "O" and gameBoard[2][2] == "O":
        print("O has won!")
        return "O"
    # Y axis
    if gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X":
        print("X has won!")
        return "X"
    elif gameBoard[0][0] == "O" and gameBoard[1][0] == "O" and gameBoard[2][0] == "O":
        print("O has won!")
        return "O"
    elif gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X":
        print("X has won!")
        return "X"
    elif gameBoard[0][1] == "O" and gameBoard[1][1] == "O" and gameBoard[2][1] == "O":
        print("O has won!")
        return "O"
    elif gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X":
        print("X has won!")
        return "X"
    elif gameBoard[0][2] == "O" and gameBoard[1][2] == "O" and gameBoard[2][2] == "O":
        print("O has won!")
        return "O"
    # Cross wins
    elif gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X":
        print("X has won!")
        return "X"
    elif gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O":
        print("O has won!")
        return "O"
    elif gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] == "X":
        print("X has won!")
        return "X"
    elif gameBoard[0][2] == "O" and gameBoard[1][1] == "O" and gameBoard[2][0] == "O":
        print("O has won!")
        return "O"
    else:
        return "N"


leave_loop = False
turn_counter = 0

# while leave_loop == False:
while leave_loop is False:
    # It's the player's turn
    if turn_counter % 2 == 1:
        printGameBoard()
        number_picked = int(input("\nChoose a number [1-9]"))
        if number_picked >= 1 or number_picked <= 9:
            modify_array(number_picked, "X")
            posible_numbers.remove(number_picked)
        else:
            print("Invalid number")
        turn_counter += 1

    # It's the computer's turn
    else:
        while True:
            cpu_choice = random.choice(posible_numbers)
            print("\nCpu choice: ", cpu_choice)
            if cpu_choice >= 1 or cpu_choice <= 9:
                modify_array(cpu_choice, "O")
                posible_numbers.remove(cpu_choice)
                turn_counter += 1
                break

    winner = checkForWinner(game_board)
    if winner != "N":
        print("\nGame over! Thank you for playing :)")
        break
