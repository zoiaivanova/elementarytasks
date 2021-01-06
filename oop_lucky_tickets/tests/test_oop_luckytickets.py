from unittest import TestCase

from oop_lucky_tickets.decorators.ticket import validate_ticket
from oop_lucky_tickets.decorators.ticket_range import validate_ticket_range
from oop_lucky_tickets.errors.invalid_ticket_error import InvalidTicketError
from oop_lucky_tickets.errors.invalid_ticket_range_error import InvalidTicketRangeError
from oop_lucky_tickets.models.ticket import Ticket
from oop_lucky_tickets.models.ticket_range import TicketRange


class TestTicketInitializer(TestCase):
    def test_raises_error_if_not_valid_ticket(self):
        invalid_tickets = ['444', '11111111', 'asd', '13fs', '-44222', '-444444', '11111.1', '111111.0']
        with self.assertRaises(InvalidTicketError):
            for ticket in invalid_tickets:
                Ticket(ticket)

    def test_returns_ticket_if_valid(self):
        for ticket in ['012345', '546777', '000011']:
            self.assertEqual(Ticket(ticket).number, ticket)


class TestTicketRangeInitializer(TestCase):
    def test_min_number_less_than_max(self):
        self.assertIs(TicketRange('222222', '555555'))

    def test_min_number_equals_max(self):
        self.assertIsNone(validate_ticket_range('222222', '222222'))

    def test_max_number_greater_than_min(self):
        with self.assertRaises(InvalidTicketRangeError):
            validate_ticket_range('555555', '222222')

