from chessboard.constants import MENU_PROMPT_START, MENU_PROMPT_DURING_PROGRAM
from chessboard.fn_chessboard.fn_chessboard import validate_side, building_board
from errors import InvalidSideError
from interfaces import ConsoleInterface


def main(interface):
    selected_option = interface.user_input(MENU_PROMPT_START).strip().lower()

    while selected_option != 'q':
        try:
            height = validate_side(interface.user_input('Enter height of chess board: ').strip())
            width = validate_side(interface.user_input('Enter width of chess board: ').strip())
            interface.user_output(building_board(height, width))
        except InvalidSideError as error:
            interface.user_output(error)
        finally:
            selected_option = interface.user_input(MENU_PROMPT_DURING_PROGRAM).strip().lower()


if __name__ == "__main__":
    main(ConsoleInterface())
