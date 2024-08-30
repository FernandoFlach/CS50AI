from tictactoe import player, actions, result, utility, min_value, max_value, minimax, terminal, winner

import math

X = "X"
O = "O"
EMPTY = None


game = [[EMPTY,EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

final_state_board = [['O', 'X', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]

terminal_check = [['O', 'X', None], [None, 'X', 'O'], [None, 'X', None]]

print("TESTING ASIDJASJD DJAKSD")
#print("AAAAAAAAAAAAAAAAAAAAAAAAA", terminal(terminal_check))
print(winner(terminal_check))

#print(actions(final_state_board))
#print(terminal(final_state_board))

print(max_value(game)[1])

# action = (2,0)

# for action in actions(game):
#     print(result(game, action))
#print(actions(game))

#print(result(game, action))

