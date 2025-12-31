# Copyright (c) 2023, matbrgz and contributors
# For license information, please see license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
from frappe.utils import add_days, today

class TestLegalContract(FrappeTestCase):
	def test_contract_expiry(self):
		contract = frappe.new_doc("Legal Contract")
		contract.title = "Test Contract"
		contract.contract_date = today()
		contract.expiration_date = add_days(today(), 365)
		contract.save()

		self.assertEqual(contract.status, "Draft")
