class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
      for row in self.board:
        print("|".join(row))
        print("-" * 5)


    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self):
    # Check rows
      for row in self.board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
    
    # Check columns
      for col in range(3):
        if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != "":
            return self.board[0][col]

    # Check diagonals
      if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "":
        return self.board[0][0]
      if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "":
        return self.board[0][2]

      return None


    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)