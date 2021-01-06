from oop_lucky_tickets.decorators.ticket import convert_to_str_ticket_with_prepended_zeros, validate_ticket


@convert_to_str_ticket_with_prepended_zeros
@validate_ticket
class Ticket:
    """
    Ticket class has 1 property(number) and 3 methods to count the lucky tickets
    Before creating an instance of Ticket class 2 decorators
    (convert_to_str_ticket_with_prepended_zeros and validate_ticket) are called to validate incoming data.
    """
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f'Ticket {self.number}'

    def __int__(self):
        return int(self.number)

    @property
    def is_simple_lucky(self) -> bool:
        """
        :return: True if sum of first digits equals sum of last 3 digits otherwise False
        """
        ticket = [int(digit) for digit in self.number]
        return sum(ticket[3:]) == sum(ticket[:3])

    @property
    def is_complex_lucky(self) -> bool:
        """
        :return: True if sum of odd digits equals sum of even digits otherwise False
        """
        odd_digits_sum = sum([int(digit) for digit in self.number if int(digit) % 2 != 0])
        even_digits_sum = sum([int(digit) for digit in self.number if int(digit) % 2 == 0])
        return odd_digits_sum == even_digits_sum

    @property
    def is_complex_lucky_alternative(self) -> bool:
        """
        :return: True if sums of digits on position with odd and even indices equal
        otherwise False
        """
        odd_index_sum = sum([int(digit) for (index, digit) in enumerate(self.number) if index % 2 != 0])
        even_index_sum = sum([int(digit) for (index, digit) in enumerate(self.number) if index % 2 == 0])
        return odd_index_sum == even_index_sum
