from tictactoe import TicTacToe

# Create a new game instance and start playing
game = TicTacToe()
game.display_board()

while True:
    row = int(input("Enter row (0-2) for player {}: ".format(game.current_player)))
    col = int(input("Enter col (0-2) for player {}: ".format(game.current_player)))
    game.make_move(row, col)
    game.display_board()
    winner = game.check_winner()
    if winner:
        print("{} wins!".format(winner))
        break
    elif winner == "Tie":
        print("It's a tie!")
        break
