import numpy
from termcolor import colored

game_board = numpy.zeros((6, 7))
full_columns = []
game_finished = False

class Node:
    def __init__(self, matrix, pos, value, parent):
        self.matrix = matrix
        self.pos = pos
        self.value = value
        self.parent = parent


def main():
    global game_board
    global game_finished
    counter = 1
    while not game_finished:
        if counter % 2 != 0:
            pretty_print()
            print("\nFirst player: ")
            column = int(input("Select a column (a number in [0,6]): "))
            for i in range(len(full_columns)):
                if column == full_columns[i]:
                    print("Selected column is full! Pleas select another.")
                    counter += 1
                    continue
            play_disc(1, column)
            counter += 1
        else:
            pretty_print()
            print("\nSecond player: ")
            column = int(input("Select a column (a number in [0,6]): "))
            for i in range(len(full_columns)):
                if column == full_columns[i]:
                    print("Selected column is full! Pleas select another.")
                    counter += 1
                    continue
            play_disc(2, column)
            counter += 1


def play_disc(player_num, column_num):
    global game_board
    global full_columns
    global game_finished
    for i in reversed(range(0, 6)):
        if game_board[i][column_num] == 0:
            game_board[i][column_num] = player_num
            if check(i, column_num, player_num) >= 4:
                pretty_print()
                print("Player nr.{} has won!".format(player_num))
                game_finished = True
            if i == 0:
                full_columns.append(column_num)
            return


def check(i, j, p):
    vertical = check_vertical_l(i, j - 1, p) + check_vertical_r(i, j + 1, p)
    horiz = check_horiz_u(i - 1, j, p) + check_horiz_d(i + 1, j, p)
    main_diag = check_main_diag_l(i - 1, j - 1, p) + check_main_diag_r(i + 1, j + 1, p)
    inv_diag = check_inv_diag_l(i + 1, j - 1, p) + check_inv_diag_r(i - 1, j + 1, p)
    return max(max(vertical, horiz), max(main_diag, inv_diag))


def check_main_diag_l(i, j, p):
    if i >= 0 and j >= 0:
        if game_board[i][j] != p:
            return 0
        else:
            return 1 + check_main_diag_l(i - 1, j - 1, p)
    else:
        return 0


def check_main_diag_r(i, j, p):
    if i < len(game_board) and j < len(game_board[i]):
        if game_board[i][j] != p:
            return 0
        else:
            return 1 + check_main_diag_r(i + 1, j + 1, p)
    else:
        return 0


def check_inv_diag_r(i, j, p):
    if i >= 0 and j < len(game_board[i]):
        if game_board[i][j] != p:
            return 0
        else:
            return 1 + check_inv_diag_r(i - 1, j + 1, p)
    else:
        return 0


def check_inv_diag_l(i, j, p):
    if i < len(game_board) and j >= 0:
        if game_board[i][j] != p:
            return 0
        else:
            return 1 + check_inv_diag_l(i + 1, j - 1, p)
    else:
        return 0


def check_horiz_d(i, j, p):
    if i < len(game_board):
        if game_board[i][j] != p:
            return 0
        else:
            return 1 + check_horiz_d(i + 1, j, p)
    else:
        return 0


def check_horiz_u(i, j, p):
    if i >= 0:
        if game_board[i][j] != p:
            return 0
        else:
            return 1 + check_horiz_u(i - 1, j, p)
    else:
        return 0


def check_vertical_r(i, j, p):
    if j < len(game_board[0]):
        if game_board[i][j] != p:
            return 0
        else:
            return 1 + check_vertical_r(i, j + 1, p)
    else:
        return 0


def check_vertical_l(i, j, p):
    if j >= 0:
        if game_board[i][j] != p:
            return 0
        else:
            return 1 + check_vertical_l(i, j - 1, p)
    else:
        return 0


def pretty_print():
    global game_board

    print("  0   1   2   3   4   5   6  ")
    for row in game_board:
        output = "| "
        for col in row:
            if col == 0:
                output += " "
            elif col == 1:
                output += colored('O', 'red')
            else:
                output += colored('O', 'blue')
            output += " | "
        print(output)
    print("|\/\/\/\/\/\/\/\/\/\/\/\/\/\|")


main()