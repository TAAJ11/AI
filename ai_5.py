import math

# Function to check if a player has won
def evaluate(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            return 10 if row[0] == 'X' else -10

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return 10 if board[0][col] == 'X' else -10

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return 10 if board[0][0] == 'X' else -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return 10 if board[0][2] == 'X' else -10

    # No winner
    return 0

# Function to check if there are moves left
def is_moves_left(board):
    for row in board:
        if '_' in row:
            return True
    return False

# Minimax algorithm
def minimax(board, depth, is_max):
    score = evaluate(board)

    # If Maximizer has won the game
    if score == 10:
        return score - depth

    # If Minimizer has won the game
    if score == -10:
        return score + depth

    # If no more moves and no winner
    if not is_moves_left(board):
        return 0

    # If it's the maximizer's move
    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = '_'

        return best

    # If it's the minimizer's move
    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = '_'

        return best

# Function to find the best move for the maximizing player (X)
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            # Check if the cell is empty
            if board[i][j] == '_':
                # Make the move
                board[i][j] = 'X'

                # Compute the evaluation function for this move
                move_val = minimax(board, 0, False)

                # Undo the move
                board[i][j] = '_'

                # If the value of the current move is more than the best value, update best_move
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Example Tic-Tac-Toe board
board = [
    ['X', 'O', 'X'],
    ['_', 'O', '_'],
    ['_', '_', '_']
]

best_move = find_best_move(board)
print(f"The best move for 'X' is at position: {best_move}")
