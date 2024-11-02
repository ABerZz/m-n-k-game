from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    row_separator = ('+' + '-' * 7) * 3 + '+'
    row_spaces = ('|' + ' ' * 7) * 3 + '|'
    
    print(row_separator)
    
    for i in range(3):
        
        print(row_spaces)
        for j in range(3):
            print('|' + ' ' * 3 + board[i][j] + ' ' * 3, end='')
        print('|')
        print(row_spaces)
        
        print(row_separator)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    move_completed = False
    
    while move_completed is False:
        
        try:
            o = int(input('Enter your move: ')) - 1
            row = o // 3
            col = o % 3
            list_of_free_fields = make_list_of_free_fields(board)
            
            for field in list_of_free_fields:
                if (row, col) == field:
                    board[row][col] = 'O'
                    move_completed = True
                    break
            else:
                raise ValueError
        
        except ValueError:
            print('Your move is invalid.')


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    list_of_free_fields = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                list_of_free_fields.append((i, j))

    return list_of_free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    victory_r1 = True
    victory_r2 = True
    victory_r3 = True
    victory_c1 = True
    victory_c2 = True
    victory_c3 = True
    victory_d1 = True
    victory_d2 = True

    for i in range(3):

        if board[0][i] != sign: victory_r1 = False

        if board[1][i] != sign: victory_r2 = False

        if board[2][i] != sign: victory_r3 = False

        if board[i][0] != sign: victory_c1 = False

        if board[i][1] != sign: victory_c2 = False

        if board[i][2] != sign: victory_c3 = False

        if board[i][i] != sign: victory_d1 = False

        if board[i][2-i] != sign: victory_d2 = False

    return victory_r1 or victory_r2 or victory_r3 or victory_c1 or victory_c2 or victory_c3 or victory_d1 or victory_d2


def draw_move(board):
    # The function draws the computer's move and updates the board.
    list_of_free_fields = make_list_of_free_fields(board)
    i = randrange(len(list_of_free_fields))
    row, col = list_of_free_fields[i]
    board[row][col] = 'X'


game_board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

display_board(game_board)

for i in range(4):

    # Player move
    enter_move(game_board)
    display_board(game_board)

    if victory_for(game_board, 'O'):
        print('You won!')
        break

    # Computer move
    draw_move(game_board)
    display_board(game_board)

    if victory_for(game_board, 'X'):
        print('You lost!')
        break

else:
    print('It\'s a draw!')