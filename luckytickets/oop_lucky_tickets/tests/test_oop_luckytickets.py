import os
from unittest import TestCase

from parameterized import parameterized

from errors import InvalidTicketError
from errors import InvalidTicketRangeError
from luckytickets.oop_lucky_tickets.models.ticket import Ticket
from luckytickets.oop_lucky_tickets.models.ticket_range import TicketRange
from test_helpers import from_file

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), '../../test_data')


class TestTicketInitializer(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='tickets.json')['invalid_tickets'])
    def test_raises_error_if_ticket_is_invalid(self, ticket):
        with self.assertRaises(InvalidTicketError):
            Ticket(ticket)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='tickets.json')['valid_tickets'])
    def test_returns_ticket_if_valid(self, ticket):
        actual = Ticket(ticket)._number
        self.assertEqual(actual, ticket)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='tickets.json')['tickets_with_prepended_zeros'])
    def test_returns_ticket_with_prepended_zeros(self, int_ticket_number, result):
        actual = Ticket(int_ticket_number)._number
        self.assertEqual(actual, result)


class TestIsSimpleLucky(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_simple_valid'])
    def test_valid_values(self, ticket):
        self.assertTrue(Ticket(ticket).is_simple_lucky)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_simple_invalid'])
    def test_invalid_values(self, ticket):
        self.assertFalse(Ticket(ticket).is_simple_lucky)


class TestIsComplexLucky(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_complex_valid'])
    def test_valid_values(self, ticket):
        self.assertTrue(Ticket(ticket).is_complex_lucky)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_complex_invalid'])
    def test_invalid_values(self, ticket):
        self.assertFalse(Ticket(ticket).is_complex_lucky)


class TestIsComplexLuckyAlternative(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_complex_alternative_valid'])
    def test_valid_values(self, ticket):
        self.assertTrue(Ticket(ticket).is_complex_lucky_alternative)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_methods.json')['is_complex_alternative_invalid'])
    def test_invalid_values(self, ticket):
        self.assertFalse(Ticket(ticket).is_complex_lucky_alternative)


class TestTicketRange(TestCase):
    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['invalid_ticket_range'])
    def test_raises_error_if_max_number_greater_than_min(self, min_number, max_number):
        with self.assertRaises(InvalidTicketRangeError):
            TicketRange(Ticket(min_number), Ticket(max_number))

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['simple_method_data'])
    def test_when_simple_method_is_winner(self, min_number, max_number, times):
        result = str(TicketRange(Ticket(min_number), Ticket(max_number)))
        self.assertIn('Simple method has won', result)
        self.assertIn(f'Simple method ran {times} times', result)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['complex_method_data'])
    def test_when_complex_method_is_winner_and_two_tickets_equal(self, min_number, max_number, times):
        result = str(TicketRange(Ticket(min_number), Ticket(max_number)))
        self.assertIn('Complex method has won', result)
        self.assertIn(f'complex method ran {times} times', result)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['complex_alternative_data'])
    def test_when_complex_alternative_method_is_winner(self, min_number, max_number, times):
        result = str(TicketRange(min_number, max_number))
        self.assertIn('Alternative complex method has won', result)
        self.assertIn(f'alternative complex method ran {times} times', result)

    @parameterized.expand(from_file(directory=TEST_DATA_DIR, file='ticket_range.json')['draw_data'])
    def test_when_it_is_a_draw(self, min_number, max_number):
        self.assertIn('It is a draw', str(TicketRange(Ticket(min_number), Ticket(max_number))))



