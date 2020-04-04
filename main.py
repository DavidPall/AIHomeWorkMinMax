import numpy
import termcolor
from termcolor import colored

game_board = numpy.zeros((6, 7))
full_columns = []

def play_disc(player_num, column_num):
    global game_board
    global full_columns
    for i in reversed(range(0, 6)):
        if game_board[i][column_num] == 0:
            game_board[i][column_num] = player_num
            if i == 0:
                full_columns.append(column_num)
            return


def main():
    global game_board


def pretty_print(active_player):
    global game_board
    if active_player:
        print("\nMy turn!\n")
    else:
        print("\nYour turn!\n")

    print("  0   1   2   3   4   5   6  ")
    for row in game_board:
        output = "| "
        for col in row:
            if col == 0:
                output += " "
            elif col == 1:
                output += colored('O', 'red')
                # output += "O"
            else:
                output += colored('O', 'blue')
                # output += "O"
            output += " | "
        print(output)
    print("|\/\/\/\/\/\/\/\/\/\/\/\/\/\|")


# def check_if_over(game_board, )
pretty_print(True)
play_disc(1, 3)
pretty_print(False)
play_disc(2, 3)
pretty_print(True)

