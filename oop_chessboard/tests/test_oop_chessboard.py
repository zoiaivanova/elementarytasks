from unittest import TestCase
from parameterized import parameterized

from oop_chessboard.errors.invalid_side_error import InvalidSideError
from oop_chessboard.models.chessboard import Chessboard
from oop_chessboard.models.side import Side


class TestSide(TestCase):
    @parameterized.expand(['-1', '0', 'abcd', ' ', ''])
    def test_raises_error_if_not_valid_side(self, side):
        with self.assertRaises(InvalidSideError):
            Side(side)

    @parameterized.expand(['1', '5', '20'])
    def test_returns_side_if_valid(self, side):
        actual = Side(side)._value
        self.assertEqual(actual, side)


class TestChessboard(TestCase):
    @parameterized.expand([
        ('1', '1', '*\n'),
        ('3', '5', '* * *\n * * \n* * *\n'),
        ('6', '6', '* * * \n * * *\n* * * \n * * *\n* * * \n * * *\n'),
        ('3', '8', '* * * * \n * * * *\n* * * * \n')
    ])
    def test_building_board(self, height, width, expected_board):
        actual = str(Chessboard(Side(height), Side(width)))
        self.assertEqual(actual, expected_board)
