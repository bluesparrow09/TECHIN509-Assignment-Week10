import unittest
from board import Board

class TestCheckWinner(unittest.TestCase):
    def test_winner_row(self):
        board = Board()
        board.board = [["X", "X", "X"], ["O", "", "O"], ["", "", ""]]
        self.assertEqual(board.check_winner(), "X")

    def test_winner_column(self):
        board = Board()
        board.board = [["X", "O", ""], ["X", "", "O"], ["X", "", ""]]
        self.assertEqual(board.check_winner(), "X")

    def test_winner_diagonal(self):
        board = Board()
        board.board = [["X", "", "O"], ["", "X", "O"], ["O", "", "X"]]
        self.assertEqual(board.check_winner(), "X")

    def test_no_winner(self):
        board = Board()
        board.board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.assertIsNone(board.check_winner())
