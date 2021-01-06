from oop_lucky_tickets.errors.invalid_ticket_error import InvalidTicketError


def convert_to_str_ticket_with_prepended_zeros(obj) -> callable:
    """
    :return: convert number to str and prepend with zeros if it is an int and < 100000
    otherwise just convert to str
    """
    def wrapper(number):
        if isinstance(number, int) and number < 100000:
            length = len(str(number))
            zero_length = (6 - length)
            return obj(f'{zero_length * "0"}{number}')
        return obj(str(number))
    return wrapper


def validate_ticket(obj) -> callable:
    def wrapper(number: str):
        """
        :return: return number if number is 6-digit string otherwise raise InvalidTicketError
        """
        if not (len(number) == 6 and number.isdigit()):
            raise InvalidTicketError(f'Your value {number} is invalid, a ticket should consist of 6 digits')
        return obj(number)
    return wrapper
