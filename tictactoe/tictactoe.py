"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_moves = 0
    o_moves = 0

    for row in board:
        x_moves += row.count("X")
        o_moves += row.count("O")

    if x_moves <= o_moves:
        return "X"
    else:
        return "O"
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    i, j = action

    if i not in (0, 1, 2) or j not in (0, 1, 2):
        raise IndexError
    elif board[i][j] != EMPTY:
        raise Exception
    
    else:
        new_board = copy.deepcopy(board)
        letter = player(board)
        new_board[i][j] = letter
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for winner in cells not empty
    for i in range(3):
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        elif board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # In case of winner
    if winner(board) != None:
        return True
    # In case of draw
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)

    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0
    

def max_value(state):
    
    if terminal(state):
        return utility(state)
    
    v = -math.inf
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    return v

# Goes down in the tree until it reaches terminal state, then starts going up geting the maximum score at each level


def min_value(state):

    if terminal(state):
        return utility(state)
    
    v = math.inf
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
    return v
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)

    if current_player == O:
        v = 2   # +inf
        for action in actions(board):
            z = max_value(result(board, action))
            if z < v:
                v = z
                best_action = action

        return best_action
    
    elif current_player == X:
        v = -2   # -inf
        for action in actions(board):
            z = min_value(result(board, action))
            if z > v:
                v = z
                best_action = action
        return best_action
    
