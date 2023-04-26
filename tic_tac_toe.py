#simple tic tac toe

# Function to display the current board
def display_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('--+---+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]}')

# Function to check if any player has won
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical wins
        [0, 4, 8], [2, 4, 6]             # diagonal wins
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full
def check_board_full(board):
    return all(cell != ' ' for cell in board)

# Function to get input from player
def get_player_input(player, board):
    valid_input = False
    while not valid_input:
        position = input(f'{player}, enter a position (1-9): ')
        if not position.isdigit() or int(position) < 1 or int(position) > 9:
            print('Invalid input. Please enter a number between 1 and 9.')
        elif board[int(position) - 1] != ' ':
            print('That position is already taken. Please choose another.')
        else:
            valid_input = True
    return int(position) - 1

# Main game function
def play_game():
    board = [' '] * 9
    players = ['X', 'O']
    current_player = players[0]
    while True:
        display_board(board)
        position = get_player_input(current_player, board)
        board[position] = current_player
        if check_win(board, current_player):
            print(f'{current_player} wins!')
            break
        elif check_board_full(board):
            print('Game over. It\'s a tie!')
            break
        current_player = players[(players.index(current_player) + 1) % 2]

# Start the game
play_game()
