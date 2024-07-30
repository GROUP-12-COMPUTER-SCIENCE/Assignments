
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("--|---|--")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_winner(self, player):
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        for pos in win_positions:
            if all(self.board[i] == player for i in pos):
                return True
        return False

    def is_draw(self):
        return all(cell != ' ' for cell in self.board) and not self.is_winner('X') and not self.is_winner('O')

    def get_available_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == ' ']

    def reset(self):
        self.board = [' '] * 9
        self.current_player = 'X'
