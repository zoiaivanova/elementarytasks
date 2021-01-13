from chessboard.constants import MENU_PROMPT_START, MENU_PROMPT_DURING_PROGRAM
from chessboard.oop_chessboard.models import Side, Chessboard
from errors import InvalidSideError
from interfaces import ConsoleInterface


def main(interface):
    selected_option = interface.user_input(MENU_PROMPT_START).strip().lower()

    while selected_option != 'q':
        try:
            height = Side(interface.user_input('Enter height of chess board: ').strip())
            width = Side(interface.user_input('Enter width of chess board: ').strip())
            interface.user_output(Chessboard(height, width))
        except InvalidSideError as error:
            interface.user_output(error)
        finally:
            selected_option = interface.user_input(MENU_PROMPT_DURING_PROGRAM).strip().lower()


if __name__ == "__main__":
    main(ConsoleInterface())
