from typing import Generator
from unittest import TestCase

from fn_lucky_tickets.fn_luckytickets import validate_ticket, is_simple_lucky, validate_ticket_range, is_complex_lucky, \
    is_complex_lucky_alternative, get_valid_tickets, compete_lucky_ticket_counting_functions
from oop_lucky_tickets.errors.invalid_ticket_error import InvalidTicketError
from oop_lucky_tickets.errors.invalid_ticket_range_error import InvalidTicketRangeError


class TestValidateTicket(TestCase):
    def test_raises_error_if_not_valid_ticket(self):
        invalid_tickets = ['444', '11111111', 'asd', '13fs', '-44222', '-444444', '11111.1', '111111.0', ' ', '']
        with self.assertRaises(InvalidTicketError):
            for ticket in invalid_tickets:
                validate_ticket(ticket)

    def test_returns_ticket_if_valid(self):
        for ticket in ['012345', '546777', '000011']:
            self.assertEqual(validate_ticket(ticket), ticket)


class TestValidateTicketRange(TestCase):
    def test_min_number_less_than_max(self):
        self.assertIsNone(validate_ticket_range('222222', '555555'))

    def test_min_number_equals_max(self):
        self.assertIsNone(validate_ticket_range('222222', '222222'))

    def test_max_number_greater_than_min(self):
        with self.assertRaises(InvalidTicketRangeError):
            validate_ticket_range('555555', '222222')


class TestGetValidTickets(TestCase):
    def test_returns_tickets(self):
        self.assertEqual(list(get_valid_tickets('111111', '111113')), ['111111', '111112', '111113'])

    def test_returns_tickets_with_prepended_zeros(self):
        self.assertEqual(list(get_valid_tickets('000111', '000113')), ['000111', '000112', '000113'])

    def test_result_is_generator(self):
        self.assertTrue(isinstance(get_valid_tickets('000111', '000113'), Generator))

    def test_returns_one_ticket_if_min_and_max_equal(self):
        self.assertEqual(next(get_valid_tickets('111111', '111111')), '111111')


class TestIsSimpleLucky(TestCase):
    def test_valid_values(self):
        for ticket in ['425650', '000000', '112211', '111111']:
            self.assertTrue(is_simple_lucky(ticket))

    def test_invalid_values(self):
        for ticket in ['324326', '661721', '020202']:
            self.assertFalse(is_simple_lucky(ticket))


class TestIsComplexLucky(TestCase):
    def test_valid_values(self):
        for ticket in ['202310', '000000', '487500']:
            self.assertTrue(is_complex_lucky(ticket))

    def test_invalid_values(self):
        for ticket in ['324326', '111111', '020202']:
            self.assertFalse(is_complex_lucky(ticket))


class TestIsComplexLuckyAlternative(TestCase):
    def test_valid_values(self):
        for ticket in ['002222', '000000', '585101']:
            self.assertTrue(is_complex_lucky_alternative(ticket))

    def test_invalid_values(self):
        for ticket in ['202310', '111112', '425650']:
            self.assertFalse(is_complex_lucky_alternative(ticket))


class TestCompareLuckyTicketCountingFunctions(TestCase):
    def test_when_simple_method_is_winner(self):
        result = compete_lucky_ticket_counting_functions('223334', '333222')
        self.assertIn('Simple method has won', result)
        self.assertIn('Simple method ran 6344 times', result)

    def test_when_complex_method_is_winner(self):
        result = compete_lucky_ticket_counting_functions('132020', '132020')
        self.assertIn('Complex method has won', result)
        self.assertIn('complex method ran 1 times', result)

    def test_when_complex_alternative_method_is_winner(self):
        result = compete_lucky_ticket_counting_functions('001111', '001122')
        self.assertIn('Alternative complex method has won', result)
        self.assertIn('alternative complex method ran 2 times', result)

    def test_when_it_is_a_draw(self):
        self.assertIn('It is a draw', compete_lucky_ticket_counting_functions('202310', '202310'))
