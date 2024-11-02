from random import randrange


### Variable initializations ###

m, n, k = 0, 0, 0

# Get board rows (m), columns (n) and aligned signs needed to win (k) from 
# the user
while True:
    try:
        m = int(input('Enter the number of rows: '))
        if m < 1:
            raise ValueError
        n = int(input('Enter the number of columns: '))
        if n < 1:
            raise ValueError
        if m * n > 999:
            print('Too many cells!')
            continue
        k = int(input('Enter the number of aligned signs to win: '))
        if k < 1 or k > m or k > n:
            raise ValueError
        break
    except ValueError:
        print('The number is invalid.')

# Create the board based on user inputs
board = []
for i in range(m):
    board.append([])
    for j in range(n):
        cell_num = str(i * n + j + 1)
        board[i].append(cell_num)


### Function definitions ###

# This function prints the board current status to the console
def display_board():
    row_separator = ('+' + '-' * 7) * n + '+'
    row_spaces = ('|' + ' ' * 7) * n + '|'
    
    print(row_separator)
    
    for i in range(m):
        
        print(row_spaces)
        for j in range(n):
            front_spaces = 4 - len(board[i][j])
            print('|' + ' ' * front_spaces + board[i][j] + ' ' * 3, end='')
        print('|')
        print(row_spaces)
        
        print(row_separator)        

# The function asks the turn user about their move, checks the input, and 
# updates the board according to the user's decision.
def enter_move(sign):
    move_completed = False
    
    while move_completed is False:
        
        try:
            s = int(input('Player ' + sign + ' enter your move: ')) - 1
            row = s // n
            col = s % n
            list_of_free_fields = make_list_of_free_fields()
            
            for field in list_of_free_fields:
                if (row, col) == field:
                    board[row][col] = sign
                    move_completed = True
                    break
            else:
                raise ValueError
        
        except ValueError:
            print('The move is invalid.')

# The function browses the board and builds a list of all the free squares; the 
# list consists of tuples, while each tuple is a pair of row and column numbers
def make_list_of_free_fields():
    list_of_free_fields = []
    
    for i in range(m):
        for j in range(n):
            if board[i][j] != 'X' and board[i][j] != 'O':
                list_of_free_fields.append((i, j))

    return list_of_free_fields

# The function browses the board and builds a list of all the squares
# containing the sign that is passed as the argument; the list is 
# built the same way as for the make_list_of_free_fields function
def make_list_of_signed_fields(sign):
    list_of_signed_fields = []

    for i in range(m):
        for j in range(n):
            if board[i][j] == sign:
                list_of_signed_fields.append((i, j))

    return list_of_signed_fields

# The function analyzes the board's status in order to check if 
# the player using 'O's or 'X's has won the game
def victory_for(sign):
    list_of_signed_fields = make_list_of_signed_fields(sign)

    # Walk through all signed fields to check victory conditions
    for row, col in list_of_signed_fields:
        
        # Horizontal down-ward alignment
        for i in range (1, k):
            if (col + i >= n) or (board[row][col + i] != sign):
                break
        else:
            return True
        
        # Vertical down-ward alignment
        for i in range (1, k):
            if (row + i >= m) or (board[row + i][col] != sign):
                break
        else:
            return True
        
        # Diagonal right-down-ward alignment
        for i in range (1, k):
            if (col + i >= n or row + i >= m) or board[row + i][col + i] != sign:
                break
        else:
            return True
        
        # Diagonal left-down-ward alignment
        for i in range (1, k):
            if (col - i < 0 or row + i >= m) or (board[row + i][col - i] != sign):
                break
        else:
            return True

    return False



### Core program loop ###

display_board()

for i in range(m * n):

    # Player X turn
    enter_move('X')
    display_board()

    if victory_for('X'):
        print('Player X wins!')
        break

    # Player O turn
    enter_move('O')
    display_board()

    if victory_for('O'):
        print('Player O wins!')
        break

else:
    print('It\'s a draw!')

