# Copyright (c) 2023, matbrgz and contributors
# For license information, please see license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

class TestTicket(FrappeTestCase):
	def test_ticket_creation(self):
		ticket = frappe.new_doc("Ticket")
		ticket.subject = "Test Ticket"
		ticket.priority = "High"
		ticket.save()

		self.assertEqual(ticket.status, "Open")
		self.assertEqual(ticket.priority, "High")
