import re


def main():
    menu_prompt = """
    Lucky tickets: there are 2 ways to count lucky tickets.\n
    The first one is simple (sum of first 3 numbers equals sum of second 3 numbers).
    The second method is complex (sum of even numbers equals sum of odd numbers).\n
    You need to enter minimum and maximum number of tickets. 
    The output of the program will be the info about method that has won and the number of lucky tickets in range of
    your min amd max number.

    Please enter one of the following options:

    - (press any key) to enter min and max ticket number
    - 'q' to quit

    What would you like to do? """

    selected_option = input(menu_prompt).strip().lower()

    while selected_option != 'q':
        try:
            min_number = input('Enter min ticket number: ').strip()
            validate_ticket(min_number)

            max_number = input('Enter max ticket number: ').strip()
            validate_ticket(max_number)
            validate_ticket_range(min_number, max_number)
        except ValueError as error:
            print(error)
        else:
            print(compete_lucky_ticket_counting_functions(min_number, max_number))

        # Allow the user to change their selection at the end of each iteration
        selected_option = input(menu_prompt).strip().lower()


def validate_ticket(ticket: str) -> None:
    '''
    :param ticket: string input by user for validation
    :return: True if ticket number has 6 digits otherwise False
    '''
    if not (len(ticket) == 6 and re.match(r'^[0-9]+$', ticket)):
        raise ValueError(f'Your value {ticket} is invalid, a ticket should consist of 6 digits')


def validate_ticket_range(min_number: str, max_number: str) -> None:
    if int(min_number) > int(max_number):
        raise ValueError(f'You entered invalid range of tickets: your min ticket is greater than max ticket')


def is_simple_lucky(ticket: str) -> bool:
    '''
    :param ticket: valid 6-digit string
    :return: True if sum of first digits equals sum of last 3 digits otherwise False
    '''
    ticket = [int(n) for n in ticket]
    return sum(ticket[3:]) == sum(ticket[:3])


def is_complex_lucky(ticket: str) -> bool:
    '''
    :param ticket: valid 6-digit string
    :return: True if sum of first digits equals sum of last 3 digits otherwise False
    '''
    odd = sum([int(n) for n in ticket if int(n) % 2 != 0])
    even = sum([int(n) for n in ticket if int(n) % 2 == 0])
    return odd == even


def convert_to_string_with_zeros(number: int) -> str:
    '''
    :param number: number from a given range of min and max numbers
    :return: 6-digit string prepended with zeros if input number < 100000
    :return: number in string format if number >= 100000
    '''
    if number < 100000:
        length = len(str(number))
        zero_length = (6 - length)
        return f'{zero_length * "0"}{number}'
    else:
        return str(number)


def get_valid_tickets(min_number: str, max_number: str) -> list:
    '''
    :param min_number: first number of the given ticket range
    :param max_number: last number of the given ticket range
    :return: list of 6-digit ticket strings (prepended with zeros when number is less than 100000)
    in range of min and max number
    '''
    return [convert_to_string_with_zeros(number) for number in range(int(min_number), int(max_number) + 1)]


def compete_lucky_ticket_counting_functions(min_number: str, max_number: str) -> str:
    '''
    :param min_number: first ticket number for the start of ticket range
    :param max_number: second ticket number for the end of ticket range
    :return: string of naming the winner while comparing two functions and getting the number of times each function had lucky tickets
    '''
    tickets = get_valid_tickets(min_number, max_number)
    simple_lucky_tickets = [ticket for ticket in tickets if is_simple_lucky(ticket)]
    complex_lucky_tickets = [ticket for ticket in tickets if is_complex_lucky(ticket)]
    simple_length = len(simple_lucky_tickets)
    complex_length = len(complex_lucky_tickets)
    if simple_length > complex_length:
        return f'Simple method has won. Simple method ran {simple_length} times, complex method ran {complex_length} times'
    elif simple_length < complex_length:
        return f'Complex method has won. Simple {simple_length} times, {complex_length} times'
    else:
        return f'It is a draw. Simple {simple_length} times, {complex_length} times'


if __name__ == "__main__":
    main()
