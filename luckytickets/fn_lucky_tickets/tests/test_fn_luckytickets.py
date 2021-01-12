import os
from typing import Generator
from unittest import TestCase

from parameterized import parameterized

from errors import InvalidTicketRangeError
from luckytickets.fn_lucky_tickets.fn_luckytickets import validate_ticket, is_simple_lucky, validate_ticket_range, is_complex_lucky, \
    is_complex_lucky_alternative, get_valid_tickets, compete_lucky_ticket_counting_functions
from errors import InvalidTicketError
from test_helpers import from_file

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), '../../test_data')


class TestValidateTicket(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='tickets.json')['invalid_tickets'])
    def test_raises_error_if_not_valid_ticket(self, ticket):
        with self.assertRaises(InvalidTicketError):
            validate_ticket(ticket)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='tickets.json')['valid_tickets'])
    def test_returns_ticket_if_valid(self, ticket):
        self.assertEqual(validate_ticket(ticket), ticket)


class TestValidateTicketRange(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['valid_ticket_range'])
    def test_min_number_less_than_max(self, min_ticket, max_ticket):
        self.assertIsNone(validate_ticket_range(min_ticket, max_ticket))

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['invalid_ticket_range'])
    def test_max_number_greater_than_min(self, min_number, max_number):
        with self.assertRaises(InvalidTicketRangeError):
            validate_ticket_range(min_number, max_number)


class TestGetValidTickets(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='tickets.json')['valid_ticket_range'])
    def test_returns_tickets(self, _, min_number, max_number, expected):
        self.assertEqual(list(get_valid_tickets(min_number, max_number)), expected)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='tickets.json')['for_generator'])
    def test_result_is_generator(self, min_number, max_number):
        self.assertTrue(isinstance(get_valid_tickets(min_number, max_number), Generator))


class TestIsSimpleLucky(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_simple_valid'])
    def test_valid_values(self, ticket):
        self.assertTrue(is_simple_lucky(ticket))

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_simple_invalid'])
    def test_invalid_values(self, ticket):
        self.assertFalse(is_simple_lucky(ticket))


class TestIsComplexLucky(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_complex_valid'])
    def test_valid_values(self, ticket):
        self.assertTrue(is_complex_lucky(ticket))

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_complex_invalid'])
    def test_invalid_values(self, ticket):
        self.assertFalse(is_complex_lucky(ticket))


class TestIsComplexLuckyAlternative(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_complex_alternative_valid'])
    def test_valid_values(self, ticket):
        self.assertTrue(is_complex_lucky_alternative(ticket))

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_complex_alternative_invalid'])
    def test_invalid_values(self, ticket):
        self.assertFalse(is_complex_lucky_alternative(ticket))


class TestCompareLuckyTicketCountingFunctions(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['simple_method_data'])
    def test_when_simple_method_is_winner(self, min_number, max_number, times):
        result = compete_lucky_ticket_counting_functions(min_number, max_number)
        self.assertIn('Simple method has won', result)
        self.assertIn(f'Simple method ran {times} times', result)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['complex_method_data'])
    def test_when_complex_method_is_winner(self, min_number, max_number, times):
        result = compete_lucky_ticket_counting_functions(min_number, max_number)
        self.assertIn('Complex method has won', result)
        self.assertIn(f'complex method ran {times} times', result)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['complex_alternative_data'])
    def test_when_complex_alternative_method_is_winner(self, min_number, max_number, times):
        result = compete_lucky_ticket_counting_functions(min_number, max_number)
        self.assertIn('Alternative complex method has won', result)
        self.assertIn(f'alternative complex method ran {times} times', result)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['draw_data'])
    def test_when_it_is_a_draw(self, min_number, max_number):
        self.assertIn('It is a draw', compete_lucky_ticket_counting_functions(min_number, max_number))
