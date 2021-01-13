from errors import InvalidSideError


def validate_side(side: str) -> str:
    """
    invalid -1, 0, adbc, ' '

    valid 1, 5, 20

    :param side: user input string for validation
    :return: raise ValueError if side isn't a natural positive number otherwise return side in str format
    """
    if not (side.isdigit() and int(side) >= 1):
        raise InvalidSideError(f'\nYour value {side} is invalid, a side should a natural positive number')
    return side


def building_board(height: str, width: str) -> str:
    """
    :param height: height for building a chessboard
    :param width: width for building a chessboard
    :return: string representing the chessboard with given height and width
    """
    result = ''
    for row in range(int(height)):
        for cell in range(int(width)):
            result += '*' if row % 2 == cell % 2 else ' '
        result += '\n'
    return result

