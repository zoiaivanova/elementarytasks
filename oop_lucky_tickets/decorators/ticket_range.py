from oop_lucky_tickets.errors.invalid_ticket_range_error import InvalidTicketRangeError


def validate_ticket_range(obj) -> callable:
    def wrapper(min_number, max_number):
        """
        :return: min_number and max_number if min_number is less or equals to max_number
        otherwise raise InvalidTicketRangeError
        """
        if int(min_number) > int(max_number):
            raise InvalidTicketRangeError('You entered invalid range of tickets:'
                                          ' your min ticket is greater than max ticket')
        return obj(min_number, max_number)
    return wrapper
