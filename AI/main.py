# main.py

from game import TicTacToe
from engine import bfs_all_possible_states, dfs_winning_strategy

def play_game():
    game = TicTacToe()
    while True:
        game.print_board()
        available_moves = game.get_available_moves()
        if not available_moves:
            print("The game is a draw!")
            break

        if game.current_player == 'X':
            move = int(input("Player X, enter your move (0-8): "))
        else:
            move = random.choice(available_moves)
            print(f"Player O (AI) chose move {move}")

        if move not in available_moves:
            print("Invalid move, try again.")
            continue

        game.make_move(move)
        if game.is_winner(game.current_player):
            game.print_board()
            print(f"Player {game.current_player} wins!")
            break

        game.switch_player()

def main():
    while True:
        print("\n1. Play Tic-Tac-Toe")
        print("2. Analyze all possible states with BFS")
        print("3. Check if there's a winning strategy with DFS")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            play_game()
        elif choice == '2':
            game = TicTacToe()
            states = bfs_all_possible_states(game)
            print(f"Number of unique states: {len(states)}")
        elif choice == '3':
            game = TicTacToe()
            game.make_move(0)  # Example move to start with
            print(f"Winning strategy exists: {dfs_winning_strategy(game, game.current_player)}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
