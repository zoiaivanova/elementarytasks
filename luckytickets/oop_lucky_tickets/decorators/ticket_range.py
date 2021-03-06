from errors import InvalidTicketRangeError
from luckytickets.oop_lucky_tickets.models.ticket import Ticket


def validate_ticket_range(obj) -> callable:
    def wrapper(min_number: Ticket, max_number: Ticket):
        """
        :return: min_number and max_number if min_number is less or equals to max_number
        otherwise raise InvalidTicketRangeError
        """
        if int(min_number) > int(max_number):
            raise InvalidTicketRangeError('\nYou entered invalid range of tickets:'
                                          ' your min ticket is greater than max ticket')
        return obj(min_number, max_number)
    return wrapper
