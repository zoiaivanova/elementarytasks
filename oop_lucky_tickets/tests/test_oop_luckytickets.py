from unittest import TestCase

from parameterized import parameterized

from oop_lucky_tickets.errors.invalid_ticket_error import InvalidTicketError
from oop_lucky_tickets.errors.invalid_ticket_range_error import InvalidTicketRangeError
from oop_lucky_tickets.models.ticket import Ticket
from oop_lucky_tickets.models.ticket_range import TicketRange


class TestTicketInitializer(TestCase):
    @parameterized.expand(['444', '11111111', 'asd', '13fs', '-44222', '-444444', '11111.1', '111111.0'])
    def test_raises_error_if_ticket_is_invalid(self, ticket):
        with self.assertRaises(InvalidTicketError):
            Ticket(ticket)

    @parameterized.expand(['012345', '546777', '000011'])
    def test_returns_ticket_if_valid(self, ticket):
        actual = Ticket(ticket)._number
        self.assertEqual(actual, ticket)

    @parameterized.expand([
        (1, '000001'),
        (999999, '999999')
    ])
    def test_returns_ticket_with_prepended_zeros(self, int_ticket_number, result):
        actual = Ticket(int_ticket_number)._number
        self.assertEqual(actual, result)


class TestIsSimpleLucky(TestCase):
    @parameterized.expand(['425650', '000000', '112211', '111111'])
    def test_valid_values(self, ticket):
        self.assertTrue(Ticket(ticket).is_simple_lucky)

    @parameterized.expand(['324326', '661721', '020202'])
    def test_invalid_values(self, ticket):
        self.assertFalse(Ticket(ticket).is_simple_lucky)


class TestIsComplexLucky(TestCase):
    @parameterized.expand(['202310', '000000', '487500'])
    def test_valid_values(self, ticket):
        self.assertTrue(Ticket(ticket).is_complex_lucky)

    @parameterized.expand(['324326', '111111', '020202'])
    def test_invalid_values(self, ticket):
        self.assertFalse(Ticket(ticket).is_complex_lucky)


class TestIsComplexLuckyAlternative(TestCase):
    @parameterized.expand(['002222', '000000', '585101'])
    def test_valid_values(self, ticket):
        self.assertTrue(Ticket(ticket).is_complex_lucky_alternative)

    @parameterized.expand(['202310', '111112', '425650'])
    def test_invalid_values(self, ticket):
        self.assertFalse(Ticket(ticket).is_complex_lucky_alternative)


class TestTicketRange(TestCase):
    def test_raises_error_if_max_number_greater_than_min(self):
        with self.assertRaises(InvalidTicketRangeError):
            TicketRange(Ticket('555555'), Ticket('222222'))

    def test_when_simple_method_is_winner(self):
        result = str(TicketRange(Ticket('223334'), Ticket('333222')))
        self.assertIn('Simple method has won', result)
        self.assertIn('Simple method ran 6344 times', result)

    def test_when_complex_method_is_winner_and_two_tickets_equal(self):
        result = str(TicketRange(Ticket('132020'), Ticket('132020')))
        self.assertIn('Complex method has won', result)
        self.assertIn('complex method ran 1 times', result)

    def test_when_complex_alternative_method_is_winner(self):
        result = str(TicketRange(Ticket('001111'), Ticket('001122')))
        self.assertIn('Alternative complex method has won', result)
        self.assertIn('alternative complex method ran 2 times', result)

    def test_when_it_is_a_draw(self):
        self.assertIn('It is a draw', str(TicketRange(Ticket('202310'), Ticket('202310'))))



