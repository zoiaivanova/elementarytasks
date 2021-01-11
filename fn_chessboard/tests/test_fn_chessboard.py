from unittest import TestCase

from parameterized import parameterized

from fn_chessboard.fn_chessboard import InvalidSideError, validate_side, building_board


class TestValidateSide(TestCase):
    @parameterized.expand(['-1', '0', 'abcd', ' ', ''])
    def test_raises_error_if_not_valid_side(self, side):
        with self.assertRaises(InvalidSideError):
            validate_side(side)

    @parameterized.expand(['1', '5', '20'])
    def test_returns_side_if_valid(self, side):
        actual = validate_side(side)
        self.assertEqual(actual, side)


class TestChessboard(TestCase):
    @parameterized.expand([
        ('1', '1', '*\n'),
        ('3', '5', '* * *\n * * \n* * *\n'),
        ('6', '6', '* * * \n * * *\n* * * \n * * *\n* * * \n * * *\n'),
        ('3', '8', '* * * * \n * * * *\n* * * * \n')
    ])
    def test_building_board(self, height, width, expected_board):
        self.assertEqual(building_board(height, width), expected_board)
