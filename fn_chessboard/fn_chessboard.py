from oop_chessboard.errors.invalid_side_error import InvalidSideError

PROGRAM_OPTIONS = """
    Please enter one of the following options:
    
    - (press any key) to enter height and width
    - 'q' to quit
    """
MENU_PROMPT_START = f"""
    Build a chessboard with given height and width. 
    An asterisk symbol(*) is a black cell and a space symbol( ) is a white cell
    This is an example for height = 4 and width = 12:
    * * * * * *
     * * * * * *
    * * * * * *
     * * * * * *
    {PROGRAM_OPTIONS}
    """
MENU_PROMPT_DURING_PROGRAM = f'Would you like to run this program again? {PROGRAM_OPTIONS}'


def main():
    selected_option = input(MENU_PROMPT_START).strip().lower()

    while selected_option != 'q':
        try:
            height = validate_side(input('Enter height of chess board: ').strip())
            width = validate_side(input('Enter width of chess board: ').strip())
        except InvalidSideError as error:
            print(error)
        else:
            print(building_board(height, width))
        finally:
            selected_option = input(MENU_PROMPT_DURING_PROGRAM).strip().lower()


def validate_side(side: str) -> str:
    """
    invalid -1, 0, adbc, ' '

    valid 1, 5, 20

    :param side: user input string for validation
    :return: raise ValueError if side isn't a natural positive number otherwise return side in str format
    """
    if not (side.isdigit() and int(side) >= 1):
        raise InvalidSideError(f'Your value {side} is invalid, a side should a natural positive number')
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


if __name__ == "__main__":
    main()

