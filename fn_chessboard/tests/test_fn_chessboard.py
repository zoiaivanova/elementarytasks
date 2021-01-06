from unittest import TestCase

from fn_chessboard.fn_chessboard import InvalidSideError, validate_board, building_board


class TestValidateBoard(TestCase):
    def test_raises_error_if_not_valid_side(self):
        invalid_sides = ['-1', '0', 'abcd', ' ', '']
        with self.assertRaises(InvalidSideError):
            for side in invalid_sides:
                validate_board(side)

    def test_returns_side_if_valid(self):
        for side in ['1', '5', '20']:
            self.assertEqual(validate_board(side), side)


class TestChessboard(TestCase):
    def test_building_board(self):
        expected_boards = [
            '*\n',
            '* * *\n * * \n* * *\n',
            '* * * \n * * *\n* * * \n * * *\n* * * \n * * *\n',
            '* * * * \n * * * *\n* * * * \n'
        ]
        sides_list = [('1', '1'), ('3', '5'), ('6', '6'), ('3', '8')]

        for sides, board in zip(sides_list, expected_boards):
            self.assertEqual(building_board(*sides), board)
