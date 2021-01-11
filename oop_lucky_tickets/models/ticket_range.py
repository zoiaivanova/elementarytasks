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
        self._min_number = min_number
        self._max_number = max_number
        self._simple_len = 0
        self._complex_len = 0
        self._complex_alternative_len = 0
        self._count_lucky_tickets_methods()

    def __get_valid_tickets(self) -> Generator:
        """
        :return: generator of ticket instances in the given range
        """
        return (Ticket(number) for number in range(int(self._min_number), int(self._max_number) + 1))

    def __repr__(self) -> str:
        """
        :return: string of naming the winner
        """
        result = f"""
        Simple method ran {self._simple_len} times, 
        complex method ran {self._complex_len} times,
        alternative complex method ran {self._complex_alternative_len} times.
        """
        if self._simple_len > self._complex_len and self._simple_len > self._complex_alternative_len:
            return f'Simple method has won: {result}'
        elif self._complex_len > self._simple_len and self._complex_len > self._complex_alternative_len:
            return f'Complex method has won: {result}'
        elif self._complex_alternative_len > self._simple_len and self._complex_alternative_len > self._complex_len:
            return f'Alternative complex method has won: {result}'
        else:
            return f'It is a draw: {result}'

    def _count_lucky_tickets_methods(self) -> None:
        """
        increment a counter variable when encounter a lucky ticket in corresponding function
        """
        for ticket in self.__get_valid_tickets():
            if ticket.is_simple_lucky:
                self._simple_len += 1
            if ticket.is_complex_lucky:
                self._complex_len += 1
            if ticket.is_complex_lucky_alternative:
                self._complex_alternative_len += 1
