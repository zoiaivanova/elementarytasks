from typing import Generator

from oop_lucky_tickets.decorators.ticket_range import validate_ticket_range
from oop_lucky_tickets.models.ticket import Ticket


@validate_ticket_range
class TicketRange:
    """
    TicketRange class has 2 properties (min_number and max_number) and 2 methods.
    First, compete_lucky_ticket_counting_functions, calculates number of time each counting lucky tickets method executes
    with instance of Ticket class.
    Second. get_valid_tickets, creates generator

    """
    def __init__(self, min_number: Ticket, max_number: Ticket):
        """
        :param min_number: instance of Ticket for the start of ticket range
        :param max_number: instance of Ticket for the end of ticket range
        """
        self.min_number = min_number
        self.max_number = max_number

    def __repr__(self):
        return f'Ticket range from {self.min_number} to {self.max_number}'

    def get_valid_tickets(self) -> Generator:
        """
        :return: generator of ticket instances in the given range
        """
        return (Ticket(number) for number in range(int(self.min_number), int(self.max_number) + 1))

    def compete_lucky_ticket_counting_functions(self) -> str:
        """
        :return: string of naming the winner while comparing two functions
        and getting the number of times each function had lucky tickets
        """
        simple_length = 0
        complex_length = 0
        complex_alternative_length = 0
        for ticket in self.get_valid_tickets():
            if ticket.is_simple_lucky:
                simple_length += 1
            if ticket.is_complex_lucky:
                complex_length += 1
            if ticket.is_complex_lucky_alternative:
                complex_alternative_length += 1

        result = f"""
        Simple method ran {simple_length} times, 
        complex method ran {complex_length} times,
        alternative complex method ran {complex_alternative_length} times.
        """

        if simple_length > complex_length and simple_length > complex_alternative_length:
            return f'Simple method has won: {result}'
        elif complex_length > simple_length and complex_length > complex_alternative_length:
            return f'Complex method has won: {result}'
        elif complex_alternative_length > simple_length and complex_alternative_length > complex_length:
            return f'Alternative complex method has won: {result}'
        else:
            return f'It is a draw: {result}'
