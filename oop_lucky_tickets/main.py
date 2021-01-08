from oop_lucky_tickets.errors.invalid_ticket_error import InvalidTicketError
from oop_lucky_tickets.errors.invalid_ticket_range_error import InvalidTicketRangeError
from oop_lucky_tickets.models.ticket import Ticket
from oop_lucky_tickets.models.ticket_range import TicketRange


PROGRAM_OPTIONS = """
Please enter one of the following options:

- (press any key) to enter min and max ticket number
- 'q' to quit
"""
MENU_PROMPT_START = f"""
Lucky tickets: there are 3 ways to count lucky tickets.\n
The first one is simple (sum of first 3 numbers equals sum of second 3 numbers).
The second method is complex (sum of even numbers equals sum of odd numbers).
The third method is alternative complex (sums of digits on position with odd and even indices equal)\n
You need to enter minimum and maximum number of tickets.
The output of the program will be the info about method that has won and the number of lucky tickets in range of
your min and max number. {PROGRAM_OPTIONS}
"""
MENU_PROMPT_DURING_PROGRAM = f'Would you like to run this program again? {PROGRAM_OPTIONS}'


def main():

    selected_option = input(MENU_PROMPT_START).strip().lower()

    while selected_option != 'q':
        try:
            min_number = Ticket(input('Enter min ticket number: ').strip())
            max_number = Ticket(input('Enter max ticket number: ').strip())
            print(TicketRange(min_number, max_number))
        except (InvalidTicketError, InvalidTicketRangeError) as error:
            print(error)
        finally:
            selected_option = input(MENU_PROMPT_DURING_PROGRAM).strip().lower()
