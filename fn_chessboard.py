import re


def main():
    program_options = """
    Please enter one of the following options:
    
    - (press any key) to enter height and width
    - 'q' to quit
    """

    menu_prompt_start = f"""
    Build a chessboard with given height and width. 
    An asterisk symbol(*) is a black cell and a space symbol( ) is a white cell
    This is an example for height = 4 and width = 12:
    * * * * * *
     * * * * * *
    * * * * * *
     * * * * * *
    {program_options}
    """

    menu_prompt_during_program = f"""
    Would you like to run this program one more time?
    {program_options}
    """

    selected_option = input(menu_prompt_start).strip().lower()

    while selected_option != 'q':
        try:
            height = input('Enter height of chess board: ').strip()
            validate_board(height)

            width = input('Enter width of chess board: ').strip()
            validate_board(width)
        except ValueError as error:
            print(error)
        else:
            print(building_board(height, width))
        finally:
            selected_option = input(menu_prompt_during_program).strip().lower()


def validate_board(side: str) -> None:
    '''
    :param side: user input string for validation
    :return: raise ValueError if side isn't a natural positive number otherwise return None
    '''
    if not (re.match(r'^[0-9]+$', side) and int(side) >= 1):
        raise ValueError(f'Your value {side} is invalid, a side should a natural positive number')


def building_board(height: str, width: str) -> str:
    '''
    :param height: height for building a chessboard
    :param width: width for building a chessboard
    :return: string representing the chessboard with given height and width
    '''
    result = ''
    for row in range(int(height)):
        for cell in range(int(width)):
            result += '*' if row % 2 == cell % 2 else ' '
        result += '\n'
    return result


if __name__ == "__main__":
    main()
