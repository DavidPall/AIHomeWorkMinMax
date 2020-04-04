import numpy
import termcolor
from termcolor import colored

game_board = numpy.zeros((6, 7))
full_columns = []


def main():
    global game_board


def play_disc(player_num, column_num):
    global game_board
    global full_columns
    for i in reversed(range(0, 6)):
        if game_board[i][column_num] == 0:
            game_board[i][column_num] = player_num
            if check(i, column_num, player_num):
                pretty_print()
                print("Player nr.{} has won!".format(player_num))
                exit(0)
            if i == 0:
                full_columns.append(column_num)
            return


def check(i, j, p):
    if (check_vertical_l(i, j - 1, p) + check_vertical_r(i, j + 1, p)) > 2:
        return True
    if (check_horiz_u(i - 1, j, p) + check_horiz_d(i + 1, j, p)) > 2:
        return True
    if (check_main_diag_l(i - 1, j - 1, p) + check_main_diag_r(i + 1, j + 1, p)) > 2:
        return True
    if (check_inv_diag_l(i + 1, j - 1, p) + check_inv_diag_r(i - 1, j + 1, p)) > 2:
        return True
    return False


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
