class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.current_player = "X"

    def display_board(self):
        print("   |   |   ")
        print(" {} | {} | {} ".format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(self.board[2][0], self.board[2][1], self.board[2][2]))
        print("   |   |   ")

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"
        else:
            print("That space is already taken. Try again.")

    def check_winner(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]

        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != " ":
                return self.board[0][j]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        # Check for a tie
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    return None
        return "Tie"
