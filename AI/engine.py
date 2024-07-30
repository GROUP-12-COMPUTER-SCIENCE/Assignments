
from collections import deque
from game import TicTacToe

def bfs_all_possible_states(game):
    queue = deque([game.board[:]])
    visited = set()
    all_states = []

    while queue:
        state = queue.popleft()
        state_tuple = tuple(state)
        
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        all_states.append(state)
        
        game_copy = TicTacToe()
        game_copy.board = state[:]
        game_copy.current_player = 'X' if state.count('X') <= state.count('O') else 'O'
        
        for move in game_copy.get_available_moves():
            new_state = state[:]
            game_copy.make_move(move)
            new_state[move] = game_copy.current_player
            queue.append(new_state)

    return all_states

def dfs_winning_strategy(game, current_player):
    if game.is_winner('X') or game.is_winner('O'):
        return game.is_winner(current_player)

    if game.is_draw():
        return False

    for move in game.get_available_moves():
        game_copy = TicTacToe()
        game_copy.board = game.board[:]
        game_copy.current_player = game.current_player
        game_copy.make_move(move)
        game_copy.switch_player()
        if dfs_winning_strategy(game_copy, game_copy.current_player):
            return True

    return False
