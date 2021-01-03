from typing import Generator


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
            min_number = validate_ticket(input('Enter min ticket number: ').strip())
            max_number = validate_ticket(input('Enter max ticket number: ').strip())
            validate_ticket_range(min_number, max_number)
        except ValueError as error:
            print(error)
        else:
            print(compete_lucky_ticket_counting_functions(min_number, max_number))
        finally:
            selected_option = input(MENU_PROMPT_DURING_PROGRAM).strip().lower()


def validate_ticket(ticket: str) -> str:
    """
    :param ticket: user input string for validation
    :return: raise ValueError if ticket isn't 6-digit string otherwise return None
    """
    if not (len(ticket) == 6 and ticket.isdigit()):
        raise ValueError(f'Your value {ticket} is invalid, a ticket should consist of 6 digits')
    return ticket


def validate_ticket_range(min_number: str, max_number: str) -> None:
    """
    :param min_number: user input string as min number
    :param max_number: user input string as max number
    :return: raise ValueError if min number is greater than max number otherwise None
    """
    if int(min_number) > int(max_number):
        raise ValueError('You entered invalid range of tickets: your min ticket is greater than max ticket')


def is_simple_lucky(ticket: str) -> bool:
    """
    :param ticket: valid 6-digit string
    :return: True if sum of first digits equals sum of last 3 digits otherwise False
    """
    ticket = [int(digit) for digit in ticket]
    return sum(ticket[3:]) == sum(ticket[:3])


def is_complex_lucky(ticket: str) -> bool:
    """
    :param ticket: valid 6-digit string
    :return: True if sum of odd digits equals sum of even digits otherwise False
    """
    odd_digits_sum = sum([int(digit) for digit in ticket if int(digit) % 2 != 0])
    even_digits_sum = sum([int(digit) for digit in ticket if int(digit) % 2 == 0])
    return odd_digits_sum == even_digits_sum


def is_complex_lucky_alternative(ticket: str) -> bool:
    """
    :param ticket: valid 6-digit string
    :return: True if sums of digits on position with odd and even indices equal
    otherwise False
    """
    odd_index_sum = sum([int(digit) for (index, digit) in enumerate(ticket) if index % 2 != 0])
    even_index_sum = sum([int(digit) for (index, digit) in enumerate(ticket) if index % 2 == 0])
    return odd_index_sum == even_index_sum


def convert_to_string_with_prepended_zeros(number: int) -> str:
    """
    :param number: number from a given range of min and max numbers
    :return: 6-digit string prepended with zeros if input number < 100000
    :return: number in string format if number >= 100000
    """
    if number < 100000:
        length = len(str(number))
        zero_length = (6 - length)
        return f'{zero_length * "0"}{number}'
    else:
        return str(number)


def get_valid_tickets(min_number: str, max_number: str) -> Generator:
    """
    :param min_number: first number of the given ticket range
    :param max_number: last number of the given ticket range
    :return: list of 6-digit ticket strings (prepended with zeros when number is less than 100000)
    in range of min and max number
    """
    return (convert_to_string_with_prepended_zeros(number) for number in range(int(min_number), int(max_number) + 1))


def compete_lucky_ticket_counting_functions(min_number: str, max_number: str) -> str:
    """
    :param min_number: first ticket number for the start of ticket range
    :param max_number: second ticket number for the end of ticket range
    :return: string of naming the winner while comparing two functions and getting the number of times each function had lucky tickets
    """
    simple_length = 0
    complex_length = 0
    complex_alternative_length = 0
    for ticket in get_valid_tickets(min_number, max_number):
        if is_simple_lucky(ticket):
            simple_length += 1
        if is_complex_lucky(ticket):
            complex_length += 1
        if is_complex_lucky_alternative(ticket):
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


if __name__ == "__main__":
    main()
