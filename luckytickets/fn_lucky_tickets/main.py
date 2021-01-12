from interfaces import ConsoleInterface
from luckytickets.constants import MENU_PROMPT_START, MENU_PROMPT_DURING_PROGRAM
from errors import InvalidTicketError
from errors import InvalidTicketRangeError
from luckytickets.fn_lucky_tickets.fn_luckytickets import validate_ticket, validate_ticket_range, \
    compete_lucky_ticket_counting_functions


def main(interface):
    selected_option = interface.user_input(MENU_PROMPT_START).strip().lower()
    while selected_option != 'q':
        try:
            min_number = validate_ticket(interface.user_input('Enter min ticket number: ').strip())
            max_number = validate_ticket(interface.user_input('Enter max ticket number: ').strip())
            validate_ticket_range(min_number, max_number)
        except (InvalidTicketError, InvalidTicketRangeError) as error:
            interface.user_output(error)
        else:
            interface.user_output(compete_lucky_ticket_counting_functions(min_number, max_number))
        finally:
            selected_option = interface.user_input(MENU_PROMPT_DURING_PROGRAM).strip().lower()


if __name__ == '__main__':
    main(ConsoleInterface())
