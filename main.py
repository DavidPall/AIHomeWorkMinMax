import numpy

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
