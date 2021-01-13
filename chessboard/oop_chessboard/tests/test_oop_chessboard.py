import os
from unittest import TestCase
from parameterized import parameterized

from chessboard.oop_chessboard.models import Side, Chessboard
from errors import InvalidSideError
from test_helpers import from_file

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), '../../test_data')


class TestSide(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='side.json')['invalid_side'])
    def test_raises_error_if_side_is_invalid(self, side):
        with self.assertRaises(InvalidSideError):
            Side(side)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='side.json')['valid_side'])
    def test_returns_side_if_valid(self, side):
        actual = Side(side)._value
        self.assertEqual(actual, side)


class TestChessboard(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='chessboard.json')['chessboard'])
    def test_building_board(self, height, width, expected_board):
        actual = str(Chessboard(Side(height), Side(width)))
        self.assertEqual(actual, expected_board)
