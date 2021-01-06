from unittest import TestCase

from oop_chessboard.errors.invalid_side_error import InvalidSideError
from oop_chessboard.models.chessboard import Chessboard
from oop_chessboard.models.side import Side


class TestSide(TestCase):
    def test_raises_error_if_not_valid_side(self):
        invalid_sides = ['-1', '0', 'abcd', ' ', '']
        with self.assertRaises(InvalidSideError):
            for side in invalid_sides:
                Side(side)

    def test_returns_side_if_valid(self):
        for side in ['1', '5', '20']:
            self.assertEqual(Side(side)._value, side)


class TestChessboard(TestCase):
    def test_building_board(self):
        expected_boards = [
            '*\n',
            '* * *\n * * \n* * *\n',
            '* * * \n * * *\n* * * \n * * *\n* * * \n * * *\n',
            '* * * * \n * * * *\n* * * * \n'
        ]
        sides_list = [('1', '1'), ('3', '5'), ('6', '6'), ('3', '8')]

        for (height, width), board in zip(sides_list, expected_boards):
            self.assertEqual(f'{Chessboard(Side(height), Side(width))}', board)
