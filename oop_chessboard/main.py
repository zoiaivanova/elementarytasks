from oop_chessboard.errors.invalid_side_error import InvalidSideError
from oop_chessboard.models.chessboard import Chessboard
from oop_chessboard.models.side import Side

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
            height = Side(input('Enter height of chess board: ').strip())
            width = Side(input('Enter width of chess board: ').strip())
        except InvalidSideError as error:
            print(error)
        else:
            print(Chessboard(height, width))
        finally:
            selected_option = input(MENU_PROMPT_DURING_PROGRAM).strip().lower()
