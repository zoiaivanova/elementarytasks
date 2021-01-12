from interfaces import ConsoleInterface
from luckytickets.constants import MENU_PROMPT_START, MENU_PROMPT_DURING_PROGRAM
from errors import InvalidTicketError
from errors import InvalidTicketRangeError
from luckytickets.oop_lucky_tickets.models.ticket import Ticket
from luckytickets.oop_lucky_tickets.models.ticket_range import TicketRange


def main(interface):
    selected_option = interface.user_input(MENU_PROMPT_START).strip().lower()
    while selected_option != 'q':
        try:
            min_number = Ticket(interface.user_input('Enter min ticket number: ').strip())
            max_number = Ticket(interface.user_input('Enter max ticket number: ').strip())
            interface.user_output(TicketRange(min_number, max_number))
        except (InvalidTicketError, InvalidTicketRangeError) as error:
            interface.user_output(error)
        finally:
            selected_option = interface.user_input(MENU_PROMPT_DURING_PROGRAM).strip().lower()


if __name__ == '__main__':
    main(ConsoleInterface())
