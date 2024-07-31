class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board initialized with empty spaces
        self.current_winner = None  # Track the winner!

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def print_board_nums(self):
        # Shows the board with numbers to indicate positions
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def dfs(board, letter):
    if board.current_winner:
        return 1 if board.current_winner == 'X' else -1

    if not board.empty_squares():
        return 0  # Draw

    best_score = float('-inf') if letter == 'X' else float('inf')
    for move in board.available_moves():
        board.make_move(move, letter)
        score = dfs(board, 'O' if letter == 'X' else 'X')
        board.board[move] = ' '  # Undo move
        board.current_winner = None

        if letter == 'X':
            best_score = max(best_score, score)
        else:
            best_score = min(best_score, score)

    return best_score

def find_best_move(board, letter):
    best_move = None
    best_score = float('-inf') if letter == 'X' else float('inf')
    for move in board.available_moves():
        board.make_move(move, letter)
        score = dfs(board, 'O' if letter == 'X' else 'X')
        board.board[move] = ' '  # Undo move
        board.current_winner = None

        if letter == 'X':
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move

    return best_move

def play_game():
    game = TicTacToe()
    print("Welcome to Tic Tac Toe!")
    game.print_board_nums()

    letter = 'X'  # Starting letter
    while game.empty_squares():
        if letter == 'O':  # AI's turn
            square = find_best_move(game, letter)
            print(f"AI ({letter}) moves to square {square}")
        else:  # Human's turn
            valid_move = False
            while not valid_move:
                try:
                    square = int(input(f"{letter}'s turn. Input move (0-8): "))
                    if square not in game.available_moves():
                        raise ValueError
                    valid_move = True
                except ValueError:
                    print("Invalid move. Please try again.")

        if game.make_move(square, letter):
            print(f"{letter} makes a move to square {square}")
            game.print_board()
            if game.current_winner:
                print(f"Congratulations! {letter} wins!")
                return
            letter = 'O' if letter == 'X' else 'X'  # Switch turns

    print("It's a tie!")

play_game()
