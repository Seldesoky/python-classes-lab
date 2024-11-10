class TicTacToe:
    def __init__(self):
        # Initialize an empty 3x3 board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # Set the current player to 'X' and Welcome Message
        self.current_player = 'X'
        self.welcome_message()
    
# Setting Welcome Message
    def welcome_message(self):
        print("Welcome to Tic-Tac-Toe!")
    
# Print the current state of the board in a row/column format
    def print_board(self):
        print("   A   B   C")
        for idx, row in enumerate(self.board):
            print(f"{idx + 1}  {' | '.join(row)}")
            if idx < 2:
                print("  ---+---+---")

# LOOP until a valid move is entered
    def get_move(self):
        while True:
            # Prompt the current player to enter a move in the format "A1", "B2", etc.
            move = input(f"Player {self.current_player}, enter your move (example: A1): ").upper()
            # Convert the move to uppercase for consistency
            # IF validate_move(move) returns True, else an error message indicating the move is invalid or the cell is already occupied
            if self.validate_move(move):
                return move
            else:
                print("Invalid move! Please enter a valid move (e.g., A1) or choose an empty cell.")
    
 # Move validation
    def validate_move(self, move):
        # IF move length is not 2:
        if len(move) != 2:
            return False
        # Split move into column and row parts
        column, row = move[0], move[1]
        # IF column is not in "ABC" OR row is not in "123":
        if column not in 'ABC' or row not in '123':
            return False
        # Convert row and column to board indices
        row_idx, col_idx = int(row) - 1, ord(column) - ord('A')
        # IF the cell at (row, column) is empty:
        return self.board[row_idx][col_idx] == ' '
    
# Making a move 
    def make_move(self, move):
        # Convert the move to board indices
        row_idx, col_idx = int(move[1]) - 1, ord(move[0]) - ord('A')
        # Set the cell at the specified indices to the current player's symbol
        self.board[row_idx][col_idx] = self.current_player

# check for winner comboination
    def check_for_winner(self):
        lines = self.board + [list(col) for col in zip(*self.board)]
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2 - i] for i in range(3)])
        
        # LOOP through each line in winning lines:
        # IF the line contains three of the current player's symbols:
        if any(line == [self.current_player] * 3 for line in lines):
            return True
        return False

# Check for ties
    def check_for_tie(self):
        return all(cell != ' ' for row in self.board for cell in row)

# Switiching current players
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

# LOOP until the game ends:
    def play_game(self):
        while True:
            # Display the current board
            self.print_board()
            # Message indicating the current player’s turn
            print(f"It's {self.current_player}'s turn.")
            # Check a valid move 
            move = self.get_move()
            # Update the board
            self.make_move(move)
            # Check for winner:
            if self.check_for_winner():
                # Show the final board
                self.print_board()
                # Message indicating the current player has won
                print(f"Player {self.current_player} wins!")
                break
            # ELSE IF check for tie is True:
            elif self.check_for_tie():
                # Show the final board
                self.print_board()
                # Message indicating the game ended in a tie
                print("The game ended in a tie!")
                break
            else:
                # Switch players for alternate turns
                self.switch_player()

# Main Program:
if __name__ == "__main__":
    # Create a new TicTacToe game instance
    game = TicTacToe()
    # Call play_game() to start the game
    game.play_game()
